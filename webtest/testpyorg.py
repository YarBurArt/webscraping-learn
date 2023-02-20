from unittest import main, TestCase
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(TestCase):  # as decorator what its test for unittest.main()
    def setUp(self):  # start test in unittest.main()
        # chromedriver = "H:\\code\\python\\chromedriver_win32\\chromedriver.exe"
        chromedriver = ChromeService(ChromeDriverManager().install())
        self.driver = Chrome(service=chromedriver)

    def test_search_in_python_org(self):  # body test
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)  # as assert ... not in ...
        area_search = driver.find_element("name", "q")  # find input tag
        area_search.send_keys("pycon")  # send pycon to input tag
        assert "No results found." not in driver.page_source
        area_search.send_keys(Keys.RETURN)

    def tearDown(self):  # end test in unittest.main()
        self.driver.close()  # or .quit() for go out from browser


if __name__ == '__main__':
    main()  # from unittest
