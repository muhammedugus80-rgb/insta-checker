import requests

USERNAMES = ["kullanici1"]

BOT_TOKEN = "TOKEN"
CHAT_ID = "CHAT_ID"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

for u in USERNAMES:
    r = requests.get(f"https://www.instagram.com/{u}/")

    if "Sorry, this page isn't available" not in r.text:
        send(f"{u} açıldı!")
