import unittest

from selenium.webdriver import Chrome, ChromeOptions
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
        driver.get("https://edition.cnn.com/")
        self.assertIn("CNN", driver.title)

        # ID = "id"
        # XPATH = "xpath"
        # LINK_TEXT = "link text"
        # PARTIAL_LINK_TEXT = "partial link text"
        # NAME = "name"
        # TAG_NAME = "tag name"
        # CLASS_NAME = "class name"
        # CSS_SELECTOR = "css selector"

        driver.maximize_window()
        title_news_elem = driver.find_element(By.CLASS_NAME, "cd__headline")

        # wait as time.sleep(10)
        # title_news_elem = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "cd__headline")))
        title_news_elem.click()
        # for elem in title_news_elems:
        #     elem.click()

        soup = BeautifulSoup(driver.page_source, 'lxml')
        with open('data/cnnarticles.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for text_p in soup.find_all('p', class_="paragraph"):
                writer.writerow([str(datetime.now()),
                                 soup.title.string,
                                 text_p.text])

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
