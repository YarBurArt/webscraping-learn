from bs4 import BeautifulSoup
import requests as rq
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().chrome,
}

response = rq.get("https://www.dns-shop.ru/catalog/", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
print(soup)

cats = soup.find("li")
print(cats)
