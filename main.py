import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "felipedunbar37@gmail.com"
PASSWORD = "kjtlbaavdawkxrul"


URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

response = requests.get(
    URL,
    headers={
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    },
)
soup = BeautifulSoup(response.text, "lxml")
price_tag = soup.select_one(selector="div #ppd span .a-offscreen")
price_text = price_tag.get_text()
price = price_text.split("$")[1]
print(price)
