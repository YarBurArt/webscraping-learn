import unittest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time
import json


class MyTestCase(unittest.TestCase):
    """
    it is more convenient for me to 
    work with selenium through the test
    """
    def setUp(self):
        # selenium initialization and its settings
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
        time.sleep(10)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        # print(soup)
        description = soup.find("p", class_="collapsable__text").text
        print(description)

        data = []
        tables = soup.find_all('table', class_="product-params__table")
        for table in tables:
            table_body = table.find('tbody')

            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])  # Get rid of empty values

        print(data)

        out_data = {
            "description": description,
            "params": data,
        }
        out_data = json.dumps(out_data, sort_keys=False,
                              indent=4, ensure_ascii=False).encode("utf8")
        with open("data/wldt.json", "w") as write_file:
            json.dump(out_data, write_file)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
