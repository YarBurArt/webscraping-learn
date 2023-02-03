# short mini parser

import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://pythonru.com/biblioteki/parsing-na-python-s-beautiful-soup"
page = rq.get(url)
soup = bs(page.text, "lxml")
print(soup)

shoto = soup.find('p')
print(shoto.text)

