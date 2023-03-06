import requests as rq
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import json

from progress.bar import Bar

bar = Bar("Check and downloading", max=1000000)


def stolen_library():
    data = []
    for work in range(1, 1000):
        for page in range(1, 1000):
            # page = 1 / work = 1
            url = f"https://ilibrary.ru/text/{str(work)}/p.{str(page)}/index.html"
            try:
                page_html = rq.get(url)
                bar.next()
            except rq.exceptions.InvalidURL:
                bar.next()
                break
            if page_html.status_code != 200:
                bar.next()
                break

            soup = BeautifulSoup(page_html.text, 'lxml')
            outtext = ''

            for pargf in soup.find_all('span', class_='p'):
                outtext += pargf.text

            translator = GoogleTranslator(source='auto', target='en')

            # translate_text = translator.translate(outtext)
            # print(outtext)
            # ot_text = ""
            # for i in outtext.split("."):
            #     ot_text = ot_text + translator.translate(i) + "."

            strip_title = soup.title.text.replace('. Текст произведения', '').replace(' ', '').lower()
            trans_title = translator.translate(strip_title)
            print(trans_title)

            data.append({
                "title": trans_title,
                "page": page,
                "link": url,
                # "body": outtext,
            })

        with open(f"data/lib_pg_book.json", 'a', encoding="utf-8") as file:
            json.dump(data, file,
                      ensure_ascii=False)

    bar.finish()


if __name__ == '__main__':
    stolen_library()

