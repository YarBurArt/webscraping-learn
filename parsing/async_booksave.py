# -*- coding: utf-8 -*-
""" Made by YarBurArt
save web library sketch
Special code style: Chinese pasta
"""
import asyncio
import json
import aiohttp
from aiohttp.http_exceptions import InvalidURLError

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

from progress.bar import Bar


progress_bar = Bar("Check and downloading", max=1000000)


async def stolen_library() -> None:
    """
    The function runs through all possible library pages
    and downloads existing ones
    :return: None
    """
    data = []
    async with aiohttp.ClientSession() as session:
        for work in range(1, 1000):
            for page in range(1, 1000):
                # page = 1 / work = 1
                url = f"https://ilibrary.ru/text/{str(work)}/p.{str(page)}/index.html"
                try:
                    async with session.get(url) as response:
                        if response.status != 200:
                            progress_bar.next()
                            break
                        progress_bar.next()

                        html = await response.text()
                        soup = BeautifulSoup(html, 'lxml')
                        outtext = ''

                        for pargf in soup.find_all('span', class_='p'):
                            outtext += pargf.text

                        translator = GoogleTranslator(source='auto', target='en')

                        strip_title = await soup.title.text.replace('. Текст произведения', '')\
                            .replace(' ', '').lower()
                        trans_title = translator.translate(strip_title)
                        print(trans_title)

                        data.append({
                            "title": trans_title,
                            "page": page,
                            "link": url,
                            "body": outtext,
                        })
                except InvalidURLError as e_invalid:
                    print(e_invalid, "go next")
                    progress_bar.next()
                    break

            with open("data/test_pg_book.json", 'a',
                      encoding="utf-8") as file:
                json.dump(data, file,
                          ensure_ascii=False)

    progress_bar.finish()


if __name__ == '__main__':
    asyncio.run(stolen_library())
