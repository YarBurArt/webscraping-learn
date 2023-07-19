import json
import logging

import requests as rq
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

from progress.bar import Bar


logging.basicConfig(level=logging.INFO, filename="logs/booksave_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("start app")
bar = Bar("Check and downloading", max=10000)


def stolen_library():
    data = []
    for work in range(1, 1000):
        for page in range(1, 1000):
            # page = 1 / work = 1
            url = f"https://ilibrary.ru/text/{str(work)}/p.{str(page)}/index.html"
            try:
                page_html = rq.get(url)
                bar.next()
                logging.info(f"OK request url: {url}")
            except rq.exceptions.InvalidURL:
                bar.next()
                logging.info(f"Invalid url: {url}")
                break
            if page_html.status_code != 200:
                bar.next()
                logging.info(f"Unsuccessful request by url: {url}")
                break

            soup = BeautifulSoup(page_html.text, 'lxml')
            outtext = ''
            try:
                for pargf in soup.find_all('span', class_='p'):
                    outtext += pargf.text
            except (AttributeError, TypeError) as e:
                logging.error("CSS selector ERROR")

            translator = GoogleTranslator(source='auto', target='en')

            # translate_text = translator.translate(outtext)
            # print(outtext)
            # ot_text = ""
            # for i in outtext.split("."):
            #     ot_text = ot_text + translator.translate(i) + "."

            strip_title = soup.title.text.replace('. Текст произведения', '').replace(' ', '').lower()
            trans_title = translator.translate(strip_title)
            print(trans_title)
            logging.debug("text translated")

            data.append({
                "title": trans_title,
                "page": page,
                "link": url,
                # "body": outtext,
            })
        try:
            with open(f"data/lib_pg_book.json", 'a', encoding="utf-8") as file:
                json.dump(data, file,
                          ensure_ascii=False)
            logging.info("File saved successfully")
        except (FileExistsError, OSError, InterruptedError) as e:
            logging.error("File was not saved, ERROR: {e}")

    bar.finish()


if __name__ == '__main__':
    try:
        stolen_library()
        logging.info("down app")
    except KeyboardInterrupt as e:
        logging.warning("Stopped from user")
