# -*- coding: utf-8 -*-
from sys import platform
import os
import requests


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

    create_article_url = create_article_url + '}]&return_content=true'
    page = requests.get(create_article_url)
    print(page.text, page.json())


if __name__ == '__main__':
    create_article('hueta', 'a magic word')

