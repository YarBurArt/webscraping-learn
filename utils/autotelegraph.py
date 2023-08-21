# -*- coding: utf-8 -*-
from sys import platform
import os
import aiohttp
import asyncio
import requests
from transliterate import translit


session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=372,
    pool_maxsize=372)
session.mount('https://', adapter)

login_url = "https://api.telegra.ph/createAccount?short_name=Sandbox&author_name=Anonymous"
token_i = requests.get(login_url).json()["result"]["access_token"]
print(token_i)


def create_article(title, *paragraph):
    """
    :param title: article title
    :param paragraph: dict like {"tag":"p","children":"Hello,+world!"}
    :return: open article or content
    """
    title = title.replace(' ', '+')
    create_article_url = 'https://api.telegra.ph/createPage?access_token=' + str(token_i) + '' \
        '&title='+title+'&author_name=Anonymous&content=[{"tag":"p",'

    for children in paragraph:
        children = children.replace(' ', '+')
        create_article_url = create_article_url + \
            '"children":["' + children + '"],'

    create_article_url += '}]&return_content=true'
    page = requests.get(create_article_url)
    print(page.text, page.json())


def search_article(article_name:str=u"анонимность", request_language:str="ru") -> list[str]:
    base_utl = "https://telegra.ph/"
    req_name = article_name
    result_pages = []
    
    if request_language != "en":
        req_name = translit(article_name, request_language, reversed=True)
    
    req_name = req_name.replace(" ", "-")
    for i in range(1, 13):
        for j in range(1, 32):
            url = base_utl + req_name + '-' + str(i) + '-' + str(j)
            status = session.get(url, timeout=5).status_code
            if status == 404:
                print("The page does not exist: " + url)
            if status == 200:
                print("OK: " + url)
                result_pages.append(url)
            else:
                pass
    
    return result_pages


async def get_article(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return url


def search_article2(article_name:str=u"анонимность", request_language:str="ru") -> list[str]:
    """The function for search the article on telegraph, telegraph search"""
    base_utl = "https://telegra.ph/"
    req_name = article_name
    all_pages = []
    loop = asyncio.get_event_loop()
    
    if request_language != "en":
        req_name = translit(article_name, request_language, reversed=True)
    
    req_name = req_name.replace(" ", "-")
    for i in range(1, 13):
        for j in range(1, 32):
            url = base_utl + req_name + '-' + str(i) + '-' + str(j)
            all_pages.append(url)
        
    coroutines = [get_article(i) for i in all_pages]
    results = loop.run_until_complete(asyncio.gather(*coroutines))
    
    return set(results)


if __name__ == '__main__':
    # create_article('hueta', 'a magic word')
    # pages = search_article("Anonymous", request_language="en")
    pages = search_article2("Anonymous", request_language="en")
    for i in pages:
        print(i)
    print("Count pages: ", len(pages))
