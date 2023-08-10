# -*- coding: utf-8 -*-
""" Made by YarBurArt
parsing google search sketch
"""
import json
import requests
from bs4 import BeautifulSoup


query = input('Search: ')
query = query.replace(' ', '+')
url = f"https://google.com/search?q={query}"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
SNEW_CLASS = 'kvH3mc'  # edit if don't work

page = requests.get(url, headers=headers, timeout=10)


def search_results(bs_page, cls, is_save=False) -> list[dict]:
    """
    :param bs_page: search page html
    :param cls: class of elem in results
    :param is_save: save results to data?
    :return: list of headers results as json
    """
    results = []
    for i in bs_page.find_all('div', class_=cls):
        anchors = i.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = i.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    if is_save:
        with open(f"data/{query}_go.json", "w", encoding="utf-8") as write_file:
            json.dump(res, write_file)
    return results


if __name__ == "__main__":
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "lxml")
        res = search_results(soup, SNEW_CLASS)
        print(res)
