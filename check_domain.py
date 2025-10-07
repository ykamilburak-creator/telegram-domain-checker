import os
import requests
from telegram import Bot

BOT_TOKEN = os.environ.get("7693666210:AAEGwalMEFXh83VTLI4sahGdITEYL8X84f0")
CHAT_ID = os.environ.get("7474293121")
DOMAIN = os.environ.get("DOMAIN")
CHECK_TYPE = os.environ.get("CHECK_TYPE", "http")

bot = Bot(token=BOT_TOKEN)

def check_domain():
    url = f"http://{DOMAIN}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            message = f"Domain kontrolü: {DOMAIN}\nTip: {CHECK_TYPE}\nDurum: ✅ Site YUKARI\nDetay: HTTP 200 - OK"
        else:
            message = f"Domain kontrolü: {DOMAIN}\nTip: {CHECK_TYPE}\nDurum: ⚠️ Site AŞAĞI\nDetay: HTTP {response.status_code}"
    except Exception as e:
        message = f"Domain kontrolü: {DOMAIN}\nTip: {CHECK_TYPE}\nDurum: ⚠️ Site AŞAĞI\nDetay: {str(e)}"
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    check_domain()
