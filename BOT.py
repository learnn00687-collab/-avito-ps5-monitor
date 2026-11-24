import os
import json
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"}
    )

    urllib.request.urlopen(request)

if __name__ == "__main__":
    send_message(
        "🎮 AvitoMonitor запущен!\n"
        "Готовим поиск PlayStation 5 до 68 000 ₽."
    )
