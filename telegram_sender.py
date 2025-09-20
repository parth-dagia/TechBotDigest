import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    allowed_tags = ['b', 'i', 'u', 'a', 'code', 'pre', 'strong', 'em']
    
    for tag in soup.find_all():
        if tag.name not in allowed_tags:
            tag.unwrap()  # removes the tag but keeps the text
    
    return str(soup)

def send_message_to_telegram(message):
    cleaned_message = clean_html(message)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": cleaned_message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True  # Optional, hides link previews for cleaner look
    }
    response = requests.post(url, data=payload)
    print("📬 Telegram response:", response.status_code, response.text)
