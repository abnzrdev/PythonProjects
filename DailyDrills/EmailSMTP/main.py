"""
Spiritual Message Email Sender.
Sends HTML-formatted emails with prayers and biblical verses.
"""
import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

# Amharic Days

AMHARIC_DAYS = [
    "ሰኞ",     # Monday
    "ማክሰኞ",  # Tuesday
    "ረቡዕ",    # Wednesday
    "ሐሙስ",    # Thursday
    "ዓርብ",    # Friday
    "ቅዳሜ",    # Saturday
    "እሁድ",    # Sunday
]

def amharic_weekday(date_obj: dt.date | dt.datetime | None = None) -> str:
    """
    Return the Amharic weekday name for the given date/datetime object.
    Defaults to current date if no date_obj is provided.
    Uses AMHARIC_DAYS mapping to convert weekday index to Amharic name."""
    if date_obj is None:
        date_obj = dt.datetime.now()
    return AMHARIC_DAYS[date_obj.weekday()]

# Email Credentials
MY_EMAIL = "your email"
PASSWORD = "your app password"


def weekday_name(date_obj: dt.date | dt.datetime | None = None) -> str:
    """
    Convert date/datetime object to English weekday name (e.g., 'Monday').
    Defaults to current date if no date_obj is provided.
    Returns a string representation of the weekday."""
    if date_obj is None:
        date_obj = dt.datetime.now()
    return date_obj.strftime("%A")

def load_text_file(path: str) -> str:
    """
    Load and return contents of a text file with UTF-8 encoding.
    Strips whitespace from beginning and end of file content.
    Returns empty string gracefully if file is not found."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def create_html_email(prayer_text: str, verse_text: str, amharic_day: str, english_day: str) -> str:
    """
    Generate beautifully formatted HTML email with prayer and biblical verse.
    Includes responsive design, gradient backgrounds, bilingual headers (English/Amharic).
    Returns complete HTML string ready to be sent via email."""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 650px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            }}
            .header {{
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                padding: 40px 20px;
                text-align: center;
            }}
            .header h1 {{
                margin: 0;
                font-size: 32px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
            .header . emoji {{
                font-size: 50px;
                margin-bottom: 10px;
            }}
            . header .subtitle {{
                margin: 10px 0 0 0;
                font-size: 18px;
                opacity: 0.95;
            }}
            .prayer-section {{
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                padding: 35px;
                border-left: 6px solid #f5576c;
                margin: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .prayer-section h2 {{
                color: #c44569;
                margin-top: 0;
                font-size: 26px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .prayer-text {{
                color: #2c2c2c;
                line-height: 2;
                font-size: 16px;
                white-space: pre-line;
                text-align: justify;
            }}
            .verse-section {{
                background: linear-gradient(135deg, #e0f7fa 0%, #e1bee7 100%);
                padding: 35px;
                margin: 25px;
                border-left: 6px solid #667eea;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .verse-section h2 {{
                color: #5e35b1;
                margin-top: 0;
                font-size: 26px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .verse-text {{
                color: #1a237e;
                font-size: 20px;
                line-height: 2;
                font-weight: 500;
                border-left: 4px solid #f093fb;
                padding-left: 25px;
                margin: 20px 0;
                font-family: 'Georgia', serif;
            }}
            .footer {{
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                padding: 30px 20px;
                text-align: center;
                color: #555;
            }}
            .footer . blessing {{
                font-size: 22px;
                color: #764ba2;
                font-weight: bold;
                margin-bottom: 15px;
            }}
            . footer p {{
                margin: 10px 0;
                line-height: 1.6;
            }}
            .footer . sent {{
                margin-top: 20px;
                color: #999;
                font-size: 12px;
                font-style: italic;
            }}
            .divider {{
                height: 3px;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
                margin: 20px 0;
            }}
            .scripture-ref {{
                text-align: right;
                font-size: 14px;
                color: #666;
                margin-top: 15px;
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="header">
                <div class="emoji">🌅✨</div>
                <h1>የ{amharic_day} መንፈሳዊ መልዕክት</h1>
                <p class="subtitle">{english_day} Spiritual Message</p>
                <p class="subtitle" style="font-size: 14px; margin-top: 5px;">
                    Start your week with prayer and God's Word
                </p>
            </div>

            <!-- Prayer Section -->
            <div class="prayer-section">
                <h2><span>🙏</span> የዛሬ ጸሎት | Today's Prayer</h2>
                <div class="divider"></div>
                <div class="prayer-text">{prayer_text}</div>
            </div>

            <!-- Verse Section -->
            <div class="verse-section">
                <h2><span>📖</span> የዛሬ ቃል | Verse of the Day</h2>
                <div class="divider"></div>
                <div class="verse-text">{verse_text}</div>
            </div>

            <!-- Footer -->
            <div class="footer">
                <div class="blessing">✨ ተባረክ!  Be Blessed! ✨</div>
                <p><strong>May this week bring you:</strong></p>
                <p>🕊️ Peace in your heart<br>
                💪 Strength for your journey<br>
                ✝️ Closeness to God's presence</p>
                <p style="margin-top: 20px; font-weight: bold; color: #764ba2;">
                    አሜን!  Amen!
                </p>
                <p class="sent">Sent with ❤️</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

def build_message(sender: str, recipient: str, subject: str, html_content: str) -> MIMEMultipart:
    """
    Build a MIME multipart message with HTML content and proper email headers.
    Attaches HTML content as email body with UTF-8 encoding.
    Returns formatted MIMEMultipart object ready for SMTP transmission."""
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    part = MIMEText(html_content, "html", "utf-8")
    msg.attach(part)
    return msg

def send_email(
    recipient: str,
    subject: str,
    html_content: str,
    sender: str = MY_EMAIL,
    password: str = PASSWORD,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
) -> None:
    """
    Send an HTML email via Gmail SMTP with SSL/TLS encryption.
    Supports both SSL (port 465) and STARTTLS (port 587) connection modes.
    Raises RuntimeError if password is not set, otherwise sends email silently."""
    if not password:
        raise RuntimeError("Email password not set. Set environment variable EMAIL_PASSWORD.")
    msg = build_message(sender, recipient, subject, html_content)
    context = ssl.create_default_context()
    if smtp_port == 465:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
    else:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())

if __name__ == "__main__":
    prayer = load_text_file("prayer.txt") or "No prayer found. Place `prayer.txt` in the project root."
    verses_raw = load_text_file("quotes.txt") or "No verse found. Place `verse.txt` in the project root."
    verses = [v.strip() for v in verses_raw.splitlines() if v.strip()]
    verse = random.choice(verses) if verses else verses_raw
    today = dt.datetime.now()
    day = weekday_name(today)
    html_content = create_html_email(prayer, verse, amharic_weekday(today), day)

    recipient = "ciert.abeni@gmail.com"
    subject = f"{day} Spiritual Message"
    send_email(recipient, subject, html_content)
    print("Email sent to", recipient)