# -*- coding: utf-8 -*-
""" Made by YarBurArt
parsing avito sketch 0.1
"""
from bs4 import BeautifulSoup
import requests

url = "https://www.avito.ru/all/avtomobili?cd=1&p="
data = {
    "auto": {}
}

for i in range(2, 100):
    page = requests.get(url + str(i), timeout=10)
    soup = BeautifulSoup(page.text, "lxml")
    links = soup.find_all("a", class_="link-link-MbQDP")

    for link in links:
        print("https://www.avito.ru"+link["href"])

# TODO
