# Email SMTP - Spiritual Message Email Sender 📧

A Python application that sends beautifully formatted HTML emails containing daily spiritual messages, prayers, and biblical verses. The project features bilingual support (English and Amharic) and utilizes Gmail's SMTP server for email delivery.

## 📋 Features

- **HTML Email Formatting**: Sends richly formatted emails with gradient backgrounds, responsive design, and professional styling
- **Bilingual Support**: Includes both English and Amharic text for weekday names and spiritual content
- **Daily Messages**: Sends prayers and biblical verses from `prayer.txt` and `quotes.txt`
- **Secure Authentication**: Uses Gmail's SMTP server with app-specific password authentication
- **SSL/TLS Encryption**: Establishes secure connections for email transmission
- **Utility Functions**: 
  - Converts dates to both English and Amharic weekday names
  - Loads text files with UTF-8 encoding
  - Creates beautifully formatted HTML emails with gradient designs

## 📦 Dependencies

- Python 3.7+
- Built-in libraries:
  - `smtplib` - SMTP protocol for sending emails
  - `email.mime` - Email message formatting
  - `ssl` - Secure socket layer for encrypted connections
  - `datetime` - Date and time handling
  - `random` - Random selection of quotes

No external dependencies required!

## 🚀 Getting Started

### Prerequisites

1. A Gmail account with an [App-Specific Password](https://support.google.com/accounts/answer/185833) generated
2. Python 3.7 or higher installed on your system
3. The project files in your local directory

### Installation

1. Clone or download the project files
2. Navigate to the EmailSMTP directory:
   ```bash
   cd path/to/EmailSMTP
   ```

### Configuration

Before running the script, you need to update the email credentials in `main.py`:

```python
MY_EMAIL = "your-email@gmail.com"
PASSWORD = "your-app-specific-password"
```

**Important**: Use an [App-Specific Password](https://support.google.com/accounts/answer/185833) from your Gmail account, not your regular password.

### Usage

Run the script from the command line:

```bash
python main.py
```

The script will:
1. Load prayer and verse texts from the text files
2. Generate an HTML-formatted email with the current day's information
3. Connect to Gmail's SMTP server
4. Send the email securely

## 📬 Email Content

The generated emails include:

- **Header Section**: Bilingual greeting with current weekday (English & Amharic)
- **Prayer Section**: Full prayer text with decorative gradient background
- **Verse Section**: A randomly selected biblical verse or spiritual quote

## 🎨 HTML Styling

The emails feature:
- Linear gradient backgrounds (purple/pink theme)
- Responsive design that works on all email clients
- Color-coded sections for prayers and verses
- Professional typography with proper spacing
- Shadow effects and rounded corners for modern appearance

## 🔐 Security

- Uses SSL/TLS encryption for SMTP connections
- Credentials should be stored securely (consider using environment variables for production)
- Never commit sensitive credentials to version control

## 💡 Key Functions

### `amharic_weekday(date_obj)`
Converts a date object to its Amharic weekday name.

### `weekday_name(date_obj)`
Converts a date object to its English weekday name.

### `load_text_file(path)`
Loads and returns the contents of a text file with UTF-8 encoding.

### `create_html_email(prayer_text, verse_text, amharic_day, english_day)`
Generates beautifully formatted HTML email content.

## 📝 Content Files

### `prayer.txt`
Contains the full prayer text in Amharic (Psalm 51 from the Bible)

### `quotes.txt`
Contains multiple biblical verses and spiritual quotes in Amharic, including references like:
- Psalm 23:1
- Philippians 4:13
- Romans 8:28
- John 3:16
- And more...

## 🛠️ Customization

You can customize:
- Email recipients by modifying the recipient email address
- Prayer and verse content by editing `prayer.txt` and `quotes.txt`
- HTML styling by modifying the CSS in the `create_html_email()` function
- Email subject line and greeting messages

## 📌 Notes

- The application uses Amharic biblical texts, making it particularly suited for Amharic-speaking communities
- Emails are formatted as HTML MIME objects for compatibility with all modern email clients
- The script gracefully handles missing text files by returning empty strings

## 🔗 Related Technologies

- **SMTP Protocol**: Simple Mail Transfer Protocol for email transmission
- **MIME**: Multipurpose Internet Mail Extensions for email formatting
- **SSL/TLS**: Secure Socket Layer / Transport Layer Security for encrypted connections

## 📄 License

This project is part of the "100 Days of Python" learning course.

## ✨ Future Enhancements

Potential improvements:
- Scheduled email sending using `schedule` or `APScheduler`
- Database integration to track sent emails
- Multiple recipient support
- User interface for configuration management
- Support for additional languages
- Email template customization

---

**Created as part of the 100 Days of Python learning journey** 🐍

