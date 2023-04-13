import unittest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time
import json
import pandas as pd


class MyTestCase(unittest.TestCase):
    def setUp(self):
        chromedriver = ChromeService(ChromeDriverManager().install())
        self.driver = Chrome(service=chromedriver)  # , options=chrome_options)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.wildberries.ru/catalog/124629300/detail.aspx")
        driver.maximize_window()
        time.sleep(10)
        detail_param_elem = driver.find_element(By.CLASS_NAME, "j-parameters-btn")
        detail_desc_elem = driver.find_element(By.CLASS_NAME, "j-description-btn")
        detail_param_elem.click()
        detail_desc_elem.click()
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        # print(soup)
        description = soup.find("p", class_="collapsable__text").text
        print(description)

        data = []
        result_params = {}
        tables = soup.find_all('table', class_="product-params__table")

        for table in tables:
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')

            for row in rows:
                cols = row.find_all('th')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])  # Get rid of empty values
                del cols
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])  # Get rid of empty values

        for i in range(0, len(data) - 1, 2):
            result_params[str(data[i][0])] = data[i + 1][0]

        print(data)

        out_data = {
            "description": description,
            "params": result_params,
        }

        with open("data/wldt.json", "w", encoding='utf-8') as write_file:
            json.dump(out_data, write_file, sort_keys=False,
                      indent=4, ensure_ascii=False)

        result_params["description"] = description
        out_data = {
            "name": [],
            "param": []
        }
        for x, y in result_params.items():
            out_data["name"].append(x)
            out_data["param"].append(y)

        df = pd.DataFrame(out_data)
        df.to_excel('data/wldt.xlsx')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
