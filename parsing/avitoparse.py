# web libs
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# local save libs
import json
from datetime import datetime

# for bot recognition, but it dont work
headers = {
    'User-Agent': UserAgent().chrome,
}

page = 1  # input()
city = 'perm'  # input()
type_product = 'telefony/mobile-ASgBAgICAUSwwQ2I_Dc'

# edit if avito rewrite css selectors for style
blocks_div_class = 'iva-item-body-KLUuy'
price_class = 'price-price-JP7qe'
title_class = 'link-link-MbQDP'
descr_class = 'iva-item-text-Ge6d'
end_page_class = 'pagination-item-JJq__j'

base_url = str(f"https://www.avito.ru/{city}/{type_product}?cd=1")


def get_count_page():
    # save start page to ram
    html = requests.get(base_url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    # print(html)
    # find end page on footer
    page_count = soup.find_all('span', class_=end_page_class)[-1]
    return page_count


# i2849336554 > div > div.iva-item-body-KLUuy


def get_data(page_count):
    data = []

    for page in range(1, int(page_count.text)):
        url = base_url + "&p=" + str(page)
        # save this page to ram
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        # parse products card
        blocks = soup.find_all('div', class_=blocks_div_class)

        for block in blocks:
            # write info from block to var
            price = block.find('span', {"class": price_class}).text
            title = block.find('a', {"class": title_class}).text
            description = block.find('div', {"class": descr_class}).text
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
    date = datetime.now()
    # save data to json with adding
    with open(f"data/{str(date)}_telefony.json", 'a',
              encoding="utf-8") as file:
        json.dump(data, file,
                  ensure_ascii=False)


def main():
    pages = get_count_page()
    data = get_data(pages)
    save_data(data)


if __name__ == '__main__':
    main()
