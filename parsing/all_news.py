# -*- coding: utf-8 -*-
""" Made by YarBurArt
news parser sketch
"""
import asyncio
from deep_translator import GoogleTranslator
import requests as rq
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


headers = {
    'User-Agent': UserAgent().chrome,
}
print("Loading . . .")


async def get_news(url: str, class_name: str, name_news: str, lang_out_text: str) -> None:
    """
    The function of receiving and translating news
    :param url: source
    :param class_name: news blocks
    :param name_news: source header
    :param lang_out_text: output language
    :return: None
    """
    response = rq.get(url, headers=headers, timeout=10)
    soup = bs(response.text, "lxml")
    title = soup.find_all("h3", class_=class_name)
    title = title[:-5] if len(title) > 10 else title

    for i in title:
        await asyncio.sleep(0)
        trans = GoogleTranslator(source='auto', target=lang_out_text).translate(i.text)
        print(trans + " | " + name_news)


task = asyncio.create_task(get_news())
try:
    asyncio.run(task)
except KeyboardInterrupt:
    print("pizdec news")
