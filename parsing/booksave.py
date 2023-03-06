import requests as rq
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import json


def test_page():
    work = 1
    data = []
    for page in range(1, 1000):
        # page = 1
        url = f"https://ilibrary.ru/text/{str(work)}/p.{str(page)}/index.html"
        try:
            page_html = rq.get(url)
        except rq.exceptions.InvalidURL:
            break
        if page_html.status_code != 200:
            break

        soup = BeautifulSoup(page_html.text, 'lxml')
        outtext = ''

        for pargf in soup.find_all('span', class_='p'):
            outtext += pargf.text

        # translate_text = GoogleTranslator(source='auto', target='en').translate(outtext)
        print(outtext)

        strip_title = soup.title.text.replace('. Текст произведения', '').replace(' ', '').lower()
        trans_title = GoogleTranslator(source='auto', target='en').translate(strip_title)
        print(trans_title)

        data.append({
            "title": trans_title,
            "page": page,
            "link": url,
            "body": outtext,
        })

    with open(f"data/test_pg_book.json", 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    test_page()

