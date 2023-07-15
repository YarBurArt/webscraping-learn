from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

srvc = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=srvc, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    '''
})

try:
    driver.get("https://anycoindirect.eu")
    time.sleep(10)
    print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')

except Exception as e:
    print(e)
finally:
    driver.close()

