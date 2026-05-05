import requests
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_message(text, url):
    api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"{text}\n\n🔗 {url}",
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(api_url, json=payload, timeout=10)
        response.raise_for_status()
        print(f"[TELEGRAM] Message sent successfully.")
    except Exception as e:
        print(f"[TELEGRAM ERROR] Failed to send message: {e}")
