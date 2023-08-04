from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# The above is a simplification for installing the driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
# The above it's for web element identification, wait conditions, and wait times
import time


# Create a service object for the EdgeDriver and setup core driver object
chromedriver = EdgeService(EdgeChromiumDriverManager().install())
browser = Edge(service=chromedriver)
browser.maximize_window()

# launching the browser and waiting for the page to load fully
start_url = 'https://travel.yandex.ru/avia/'
browser.get(start_url)
WebDriverWait(browser, 10).until(
    ec.presence_of_element_located((By.TAG_NAME, "html"))
)
# get to start date
time.sleep(10)
browser.find_element(By.CLASS_NAME, "pDOJR").click()
start_date_elem = browser.find_element(By.CLASS_NAME, "INYOI")
start_date_elem.click()

# find parent month element
year_elem = browser.find_element(
    By.CSS_SELECTOR,
    "body > div.xeI0t.TravelPopup._8tU4s.popup_theme_none._9MOQ8.SjX-k > "
    "div:nth-child(2) > div > div.EhCXF.ltenZ._274Q5 > div > div.monthsList"
)
# find target months
start_month_elem = year_elem.find_element(
    By.XPATH,
    "//div[contains(text(), 'Ноябрь')]"
)
end_month_elem = year_elem.find_element(
    By.XPATH,
    "//div[contains(text(), 'Октябрь')]"
)
start_month_elem.click()
# find and click day
parent_date = browser.find_element(By.CLASS_NAME, "PFU5n")
parent_date.find_element(
    By.XPATH,
    "//div[contains(text(), '23')]"
).click()

end_month_elem.click()

parent_date.find_element(
    By.XPATH,
    "//div[contains(text(), '7')]"
).click()

input()







