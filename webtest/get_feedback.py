from unittest import main, TestCase

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium_stealth import stealth
from fake_user_agent import user_agent


class SearchFeedback(TestCase):
    def setUp(self):
        # chromedriver = "H:\\code\\python\\chromedriver_win32\\chromedriver.exe"
        options = ChromeOptions()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("start-maximized")

        chromedriver = Service(ChromeDriverManager().install())
        driver = Chrome(service=chromedriver, options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": user_agent("chrome")
        })
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            '''
        })
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,)
        self.driver = driver

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://market.yandex.ru/")
        self.assertIn("Яндекс", driver.title)
        driver.implicitly_wait(3)

        area_search = driver.find_element(By.ID, "header-search")
        area_search.send_keys("redmi 10")
        self.assertIn("No results found", driver.page_source)
        area_search.send_keys(Keys.RETURN)
        # print(driver.page_source)
        driver.implicitly_wait(5)

        self.assertIn("_2f75n", driver.page_source)
        products = driver.find_elements(By.CLASS_NAME, "_2UHry")
        for product in products:
            u_pr = product.find_element(By.TAG_NAME, "a")
            url = u_pr.get_attribute("href")
            # print(url)

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == '__main__':
    main()
