# -*- coding: utf-8 -*-
""" Made by YarBurArt
search images from folder to Yandex Search
"""
import json
import os
from pathlib import Path
import requests


def get_url_search(path, is_start_page, params):
    """
    :param path: image path
    :param is_start_page: start browser by url
    :param params: post request params, element search
    :return: None or start page
    """
    paths = [str(f.absolute()) for f in Path(path).rglob("*")]

    print("images: ", paths)

    for file_path in paths:
        search_url = 'https://yandex.ru/images/search'
        files = {'upfile': ('blob', open(file_path, 'rb'), 'image/jpeg')}
        response = requests.post(search_url, params=params,
                                 files=files, timeout=10)
        query_string = json.loads(response.content)['blocks'][0]['params']['url']

        img_search_url = search_url + '?' + query_string
        print(img_search_url)

        if is_start_page:
            os.system('start ' + img_search_url)  # TODO


if __name__ == '__main__':
    get_url_search(
        path="data\\image",
        is_start_page=False,
        params={'rpt': 'imageview',
                'format': 'json',
                'request': '{"blocks":'
                           '[{"block":"b-page_type_search-by-image__link"}]'
                '}'}
        )  # edit params or path if don't work
