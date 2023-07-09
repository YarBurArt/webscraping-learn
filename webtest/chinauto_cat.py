import unittest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import csv
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # vpn_extension_path = 'C:\\Users\\YarBurArt\\AppData\\Local\\Google\\Chrome\\User Data'
        # chrome_options = ChromeOptions()
        # chrome_options.add_argument('--user-data-dir={}'.format(vpn_extension_path))
        chromedriver = ChromeService(ChromeDriverManager().install())
        self.driver = Chrome(service=chromedriver)  # , options=chrome_options)

    def test_search(self):
        driver = self.driver
        driver.get("https://ncars.com.ua/ru/models/")

        driver.maximize_window()

        for i in range(8):
            try:
                title_news_elem = WebDriverWait(driver, 3).until(
                     EC.presence_of_element_located((By.CLASS_NAME, "next__page")))
                title_news_elem.click()
            except Exception as e:
                print(i); break
        soup = BeautifulSoup(driver.page_source, 'lxml')
        cards = soup.find_all('div', 'model__item')
        for card in cards:
            title = card.find('div', 'brand__title').find('a').text
            model = card.find('div', 'model__title').find('a').text
            print(title, model)
        # with open('data/cnnarticles.csv', 'a', newline='') as csvfile:
        #     writer = csv.writer(csvfile, delimiter=';',
        #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     for text_p in soup.find_all('p', class_="paragraph"):
        #         writer.writerow([str(datetime.now()),
        #                          soup.title.string,
        #                          text_p.text])

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()