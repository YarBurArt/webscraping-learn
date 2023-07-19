import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
import os


def get_alpha_stat(company: str = "IBM", param: str = "TIME_SERIES_INTRADAY") -> dict:
    API_KEY = os.getenv('API_KEY')
    url = f'https://www.alphavantage.co/query?function={param}&symbol={company}&interval=5min&apikey={API_KEY}'
    r = rq.get(url)
    data = r.json()

    return data


def get_table_stat():
    for page_i in range(1, 12):
        url = f'https://smart-lab.ru/q/spbex/order_by_value_today/desc/page{page_i}/'
        page = rq.get(url)
        soup = bs(page, 'lxml')

        table1 = soup.find('table', id='usa_shares')

        headers = []
        for i in table1.find_all('th'):
            title = i.text
            headers.append(title)

        mydata = pd.DataFrame(columns=headers)

        for j in table1.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            length = len(mydata)
            mydata.loc[length] = row

        mydata.to_csv('data/data_index.csv', index=False)


if __name__ == '__main__':
    pass

