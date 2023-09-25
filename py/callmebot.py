import requests
from urllib.parse import quote

PHONE_NUMER = "+5521968094745" 
CALLME_BOT_API_KEY = "Bootchat"

message = """Olá mundo!"""

requests.get(
    url="https://api.callmebot.com/whatsapp.php\
        ?phone={PHONE_NUMBER}\
        &text={quote(message)}\
        &apikey={CALLME_BOT_API_KEY}"
)
