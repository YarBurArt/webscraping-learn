from bs4 import BeautifulSoup
import requests
import json


url = "https://www.avito.ru/all/avtomobili?cd=1&p="

data = {
    "auto": {}
}

for i in range(2, 100):
    page = requests.get(url + str(i))
    soup = BeautifulSoup(page.text, "lxml")
    links = soup.find_all("a", class_="link-link-MbQDP")

    for link in links:
        print("https://www.avito.ru"+link["href"])


