import requests
import whois
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DOMAIN = os.getenv("DOMAIN", "m.bahisbudur568.com")
CHECK_TYPE = os.getenv("CHECK_TYPE", "http")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        r = requests.post(url, data=payload, timeout=15)
        return r.status_code, r.text
    except Exception as e:
        print("Telegram gönderim hatası:", e)
        return None, str(e)

def check_http(domain):
    try:
        start = time.time()
        r = requests.get("http://" + domain, timeout=15, allow_redirects=True)
        elapsed = time.time() - start
        return True, f"HTTP {r.status_code} - {r.reason} - {elapsed:.2f}s"
    except Exception as e:
        return False, str(e)

def check_whois(domain):
    try:
        w = whois.whois(domain)
        exp = getattr(w, "expiration_date", None)
        return True, f"Whois expiration: {exp}"
    except Exception as e:
        return False, str(e)

def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("BOT_TOKEN veya CHAT_ID eksik.")
        return

    if CHECK_TYPE == "http":
        ok, msg = check_http(DOMAIN)
        title = "✅ Site YUKARI" if ok else "⚠️ Site AŞAĞI / Erişilemiyor"
    else:
        ok, msg = check_whois(DOMAIN)
        title = "📄 Whois Bilgisi" if ok else "⚠️ Whois Hatası"

    text = f"*Domain kontrolü:* `{DOMAIN}`\n*Tip:* {CHECK_TYPE}\n*Durum:* {title}\n*Detay:* {msg}"
    send_telegram(text)

if __name__ == "__main__":
    main()
