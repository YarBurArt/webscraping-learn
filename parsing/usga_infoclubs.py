# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


LINK = "https://www.usga.org/InfoClubsDB/ResultDisplay.aspx?" \
       "clubtype=Wedge&Manf=Work%27s%20Inc&Prod=All"

URL_LISTS_CATEGORY = "https://www.usga.org/InfoClubsDB/Search.aspx"
PART_OPTION = 1

# print(requests.get(url_lists_category).text)
with open('data/copy_pages/'
          'search_usga_infoclubdb.html',
          'r', encoding='utf-8') as file:
    page = file.read().encode("utf-8")

soup = BeautifulSoup(page, 'lxml')

club_type, manufacturer = [], []

for i in soup.find_all('select'):
    PART_OPTION += 1
    for j in i.find_all('option'):
        if PART_OPTION == 2:
            club_type.append(j['value'])
            print(j)  # FIXME: value is not displayed
        if PART_OPTION == 3:
            manufacturer.append(j['value'])
        else:
            break

print(set(club_type))
# print(manufacturer)
# TODO: parse info by type / manufacturer
