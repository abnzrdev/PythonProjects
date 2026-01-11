import os, requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api = os.getenv("NEWSAPI_KEY")
alphavantage = os.getenv("ALPHAVANTAGE")

def get_recent_closing_prices(api_key, symbol, endpoint=STOCK_ENDPOINT, outputsize="compact"):
    """Return (close_yesterday, close_day_before) as floats, or (None, None) on error."""
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": outputsize,
    }
    try:
        resp = requests.get(endpoint, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.HTTPError as e:
        print("HTTP error while fetching stock data:", e)
        return None, None
    except requests.exceptions.Timeout:
        print("Stock request timed out")
        return None, None
    except requests.exceptions.RequestException as e:
        print("Stock request error:", e)
        return None, None
    except ValueError:
        print("Invalid JSON in stock response")
        return None, None

    ts = data.get("Time Series (Daily)", {})
    if not ts:
        return None, None

    dates = sorted(ts.keys(), reverse=True)
    if len(dates) < 2:
        return None, None

    try:
        close_yesterday = float(ts[dates[0]]["4. close"])
        close_day_before = float(ts[dates[1]]["4. close"])
    except (KeyError, ValueError):
        return None, None

    return close_yesterday, close_day_before

def has_significant_price_change(close_yesterday, close_day_before, threshold=5):
    """Return (is_significant: bool, percent_change: float) given two closing prices.

    Percent is computed as: (yesterday - day_before) / day_before * 100
    """
    if close_yesterday is None or close_day_before is None:
        return False, 0.0
    if close_day_before == 0:
        return False, 0.0

    percent = (close_yesterday - close_day_before) / close_day_before * 100
    return abs(percent) >= threshold, percent

def get_articles(api, url):
    try:
        params = {
            "q": COMPANY_NAME,
            "pageSize": 3,
            "sortBy": "publishedAt",
            "apiKey": api,
        }
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != "ok":
            print("NewsAPI error:", data.get("message"))
            return []
        return data.get("articles", [])[:3]
    except requests.exceptions.HTTPError as e:
        print("HTTP error while fetching news:", e)
    except requests.exceptions.Timeout:
        print("News request timed out")
    except requests.exceptions.RequestException as e:
        print("News request error:", e)
    except ValueError:
        print("Invalid JSON in news response")
    return []

def send_articles_via_twilio(articles):
    """Send each article (title + description) as a separate SMS via Twilio.

    Requires these environment variables:
    - TWILIO_ACCOUNT_SID
    - TWILIO_AUTH_TOKEN
    - TWILIO_FROM_NUMBER
    - MY_PHONE_NUMBER
    """
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_num = os.getenv("TWILIO_FROM_NUMBER")
    to_num = os.getenv("MY_PHONE_NUMBER")

    if not all([sid, token, from_num, to_num]):
        print("Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, MY_PHONE_NUMBER")
        return

    try:
        from twilio.rest import Client
    except ImportError:
        print("twilio package not installed. Install with: pip install twilio")
        return

    client = Client(sid, token)
    for art in articles:
        title = art.get("title", "No title")
        brief = art.get("description", "") or ""
        body = f"Headline: {title}\nBrief: {brief}"
        try:
            msg = client.messages.create(body=body, from_=from_num, to=to_num)
            print("Sent message", getattr(msg, "sid", "unknown"))
        except Exception as e:
            print("Failed to send message:", e)


if __name__ == "__main__":
    close_y, close_b = get_recent_closing_prices(alphavantage, STOCK)
    significant, percent = has_significant_price_change(close_y, close_b)
    if significant:
        print(f"Significant change detected: {percent:.2f}% — fetching news...")
        articles = get_articles(news_api, NEWS_ENDPOINT)
        if articles:
            send_articles_via_twilio(articles)
        else:
            print("No articles found to send.")
    else:
        print(f"No significant change: {percent:.2f}%")


