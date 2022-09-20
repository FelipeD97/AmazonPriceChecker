import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TEST_EMAIL = os.environ["TEST_EMAIL"]


URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_2?pd_rd_i=B08PQ2KWHS&psc=1"

response = requests.get(
    URL,
    headers={
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    },
)
soup = BeautifulSoup(response.text, "lxml")
price_tag = soup.select_one(selector="div #ppd div .a-section span .a-offscreen")
price_text = price_tag.get_text()
price = price_text.split("$")[1]
# print(price_tag)

item_tag = soup.select_one(selector="div #titleSection span")
item_name = item_tag.get_text()

if float(price) > 100:

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TEST_EMAIL,
            msg=f"Subject:Your Amazon Price Dropped\n\n The {item_name} is now {price}.\n Follow the link below to purchase now!\n {URL}".encode(
                "utf-8"
            ),
        )
