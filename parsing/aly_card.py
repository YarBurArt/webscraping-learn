# -*- coding: utf-8 -*-
""" Made by YarBurArt
script for parsing cards from alik
"""
import requests as rq
from requests.models import Response
from bs4 import BeautifulSoup

import pandas as pd

# edit if aliexpress modification style css selectors
TITLE_CLASS: str = "snow-ali-kit_Typography__base__1shggo"
PRICE_CLASS: str = "snow-price_SnowPrice__mainS__azqpin"
STATE_CLASS: str = "SnowSku_SkuPropertyItem__propNameWrap__sj6tl"

data: dict = {
    'Name': list[str],
    'Price': list[str],
    'From state': list[str]
}


def get_page() -> BeautifulSoup:
    """The function for save html page to RAM"""
    # https://aliexpress.ru/item/2044891395.html?sub=44981&utm_
    # campaign=44981&af=739_44981&aff_platform=api-new-link
    # -generate&utm_medium=cpa&sub1=1068989&cn=2ururq6bi16k03
    # uyd6y2hllw354pbvgy&dp=2ururq6bi16k03uyd6y2hllw354pbvgy&aff
    # _fcid=0ca158e4d6084f35acb0f1ada599675d-1676551609365-08780-
    # _DEkTcIR&cv=3&aff_fsk=_DEkTcIR&sk=_DEkTcIR&aff_trace_key=
    # 0ca158e4d6084f35acb0f1ada599675d-1676551609365-08780-_
    # DEkTcIR&terminal_id=ccde0aed126d4739a41595ddbbb4047c&utm
    # _content=1068989&utm_source=admitad&gatewayAdapt
    # =glo2rus&sku_id=12000024771914456
    url: str = input("url: ")
    page: Response = rq.get(url, timeout=10)
    return BeautifulSoup(page.text, 'lxml')


def find_elements(soup: BeautifulSoup) -> None:
    """The function for find elements and add to data"""

    try:
        title: str = soup.find('h1', class_=TITLE_CLASS).text
        # print(title.text)
        price: str = soup.find('div', class_=PRICE_CLASS).text
        # print(price.text)
        from_state: str = soup.find('div', class_=STATE_CLASS).text
        # print(from_state.text[11:])
        # ...
        data['Name'].append(title)
        data['Price'].append(price)
        data['From state'].append(from_state)

    except AttributeError:
        print("site block me, try add ebalay magic")


def export_exel(data_s: pd.DataFrame) -> None:
    """The function for save result"""
    data_s.to_excel("data/ali_data_product.xlsx")


if __name__ == "__main__":
    my_soup = get_page()
    find_elements(my_soup)

    if input("save (y, n)? ") == 'y':
        export_exel(data)
