from pyautogui import typewrite
import time
# auto write for zen perfect 

x1 = '''
import requests as rq 
from bs4 import BeautifulSoup as bs

url = "https://pythonru.com/biblioteki/parsing-na-python-s-beautiful-soup"
page = rq.get(url)
soup = bs(page.text, "lxml")
print(soup)

shoto = soup.find('p')
print(shoto.text)
'''
x2 = """
shoto = soup.find_all('span', class_='td-w-reb td-w-reb-id-content_top
                                      td_uid_4_61683f7d10a02_rand td_block_template_17')
print(shoto.text)"""
s1 = list(x1)
# print(s1)


def write(s, x):
    i = 0
    while i < len(x):
        n = s[i]
        typewrite(n, interval=0.10)
        # print(i)
        i += 1


time.sleep(10)
write(s1, x1)

