# -*- coding: utf-8 -*-
""" Made by YarBurArt
parsing avito sketch 0.2
"""
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# for bot recognition, but it dont work
headers = {
    'User-Agent': UserAgent().chrome,
}

PAGE = 1  # input()
CITY = 'perm'  # input()
TYPE_PRODUCT = 'telefony/mobile-ASgBAgICAUSwwQ2I_Dc'

# edit if avito rewrite css selectors for style
BLOCKS_DIV_CLASS = 'iva-item-body-KLUuy'
PRICE_CLASS = 'price-price-JP7qe'
TITLE_CLASS = 'link-link-MbQDP'
DESCR_CLASS = 'iva-item-text-Ge6d'
END_PAGE_CLASS = 'pagination-item-JJq__j'

BASE_URL = str(f"https://www.avito.ru/{CITY}/{TYPE_PRODUCT}?cd=1")


def get_count_page():
    """get count pages from pagination"""
    # save start page to ram
    html = requests.get(BASE_URL, headers=headers, timeout=10).text
    soup = BeautifulSoup(html, 'lxml')
    # print(html) debug
    # find end page on footer
    page_count = soup.find_all('span', class_=END_PAGE_CLASS)[-1]
    return page_count


def get_data(page_count):
    """get_data from page by classes"""
    data = []

    for page in range(1, int(page_count.text)):
        url = BASE_URL + "&p=" + str(page)
        # save this page to ram
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, 'lxml')
        # parse products card
        blocks = soup.find_all('div', class_=BLOCKS_DIV_CLASS)

        for block in blocks:
            # write info from block to var
            price = block.find('span', {"class": PRICE_CLASS}).text
            title = block.find('a', {"class": TITLE_CLASS}).text
            description = block.find('div', {"class": DESCR_CLASS}).text
            # print(title, " - ", price)
            # print(description)

            # add data to array of every block every page
            data.append({
                'price': price,
                'title': title,
                'description': description
            })

    return data


def save_data(data):
    """save result data to json"""
    date = datetime.now()
    # save data to json with adding
    with open(f"data/{str(date)}_telefony.json", 'a',
              encoding="utf-8") as file:
        json.dump(data, file,
                  ensure_ascii=False)


def main():
    """main flow for test"""
    pages = get_count_page()
    data = get_data(pages)
    save_data(data)


if __name__ == '__main__':
    main()
