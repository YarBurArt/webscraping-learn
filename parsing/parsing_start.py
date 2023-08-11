# mini parser
from requests import get
from bs4 import BeautifulSoup as Bs

print(Bs(get("https://u.to/4KDeHw").text, "lxml").find('p').text)
