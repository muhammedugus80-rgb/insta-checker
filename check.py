import requests

USERNAMES = ["hatjasangtar"]

BOT_TOKEN = "8904316114:AAESRD9p-eJc1xL6D0oO-UED72ceMqKQL58"
CHAT_ID = "8800074041"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

for u in USERNAMES:
    r = requests.get(f"https://www.instagram.com/{u}/")

    if "Sorry, this page isn't available" not in r.text:
        send(f"{u} açıldı!")
