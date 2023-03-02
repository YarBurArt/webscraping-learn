import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MyTestCase(unittest.TestCase):
    def setUp(self):
        chromedriver = ChromeService(ChromeDriverManager().install())
        self.driver = Chrome(service=chromedriver)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.nytimes.com/international/")
        self.assertIn("New York Times", driver.title)

        # ID = "id"
        # XPATH = "xpath"
        # LINK_TEXT = "link text"
        # PARTIAL_LINK_TEXT = "partial link text"
        # NAME = "name"
        # TAG_NAME = "tag name"
        # CLASS_NAME = "class name"
        # CSS_SELECTOR = "css selector"


        # title_news_elem = driver.find_element(By.CLASS_NAME, "css-9mylee")

        # wait as time.sleep()
        title_news_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-9mylee"))
        )
        title_news_elem.click()
        # for elem in title_news_elems:
        #     elem.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
