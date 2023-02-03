from deep_translator import GoogleTranslator
import requests as rq
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import asyncio

headers = {
    'User-Agent': UserAgent().chrome,
}
print("Loading . . .")


async def new_nt():
    response = rq.get("https://www.nytimes.com", headers=headers)
    soup = bs(response.text, "lxml")
    #print(soup)
    title = soup.find_all("h3", class_="indicate-hover")
    title = title[:-5]
    for i in title:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | nytimes.com")


async def new_ria():
    response = rq.get("https://ria.ru", headers=headers)
    soup = bs(response.text, "lxml")
    #print(soup)
    name = soup.find_all("span", class_="cell-list__item-title")
    for i in name:
        await asyncio.sleep(0)
        print(i.text + " | ria.ru")


async def new_up():
    response = rq.get("https://www.pravda.com.ua/news/", headers=headers)
    soup = bs(response.text, "lxml")
    name = soup.find_all("div", class_="article_header")
    for i in name:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | pravda.ua")


async def new_eu():
    response = rq.get("https://www.euronews24.eu/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=85&Itemid=496&lang=en", headers=headers)
    soup = bs(response.text, "lxml")
    name = soup.find_all("h3", class_="catItemTitle")
    for i in name:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | euronews24.eu")


async def new_cn():
    response = rq.get("https://www.chinadaily.com.cn/china", headers=headers)
    soup = bs(response.text, "lxml")
    name1 = soup.find_all("div", class_="tBox")
    for i in name1:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | chinadaily.com.cn")
    name2 = soup.find_all("div", class_="tBox2")
    for i in name2:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | chinadaily.com.cn")
    name3 = soup.find_all("div", class_="tBox3")
    for i in name3:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | chinadaily.com.cn")


async def new_au():
    response = rq.get("https://au.int/en/happening/news/", headers=headers)
    soup = bs(response.text, "lxml")
    name = soup.find_all("div", class_="views-field views-field-field-short-title")
    for i in name:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | au.int")


async def new_blg():
    response = rq.get("https://www.bloomberg.com", headers=headers)
    soup = bs(response.text, "lxml")
    name = soup.find_all("a", class_="story-list-story__info__headline-link")
    for i in name:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | bloomberg.com")

async def new_med():
    response = rq.get("https://meduza.io/specials/voina", headers=headers)
    soup = bs(response.text, "lxml")
    name = soup.find_all("span", class_="BlockTitle-second")
    for i in name:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | meduza.io")

async def new_cnn():
    response = rq.get("https://edition.cnn.com", headers=headers)
    soup = bs(response.text, "lxml")
    name = soup.find_all("span", class_="cd__headline-icon-vid cnn-icon")
    for i in name:
        await asyncio.sleep(0)
        tstext = i.text
        trans = GoogleTranslator(source='auto', target='ru').translate(tstext)
        print(trans + " | cnn.com")



ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(new_nt()),
    ioloop.create_task(new_ria()),
    ioloop.create_task(new_up()),
    ioloop.create_task(new_eu()),
    ioloop.create_task(new_cn()),
    ioloop.create_task(new_au()),
    ioloop.create_task(new_blg()),
    ioloop.create_task(new_med())
]
try:
    ioloop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt:
    print("pizdec news")
    exit()
finally:
    ioloop.close()
