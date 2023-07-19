from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

chromedriver = EdgeService(EdgeChromiumDriverManager().install())
driver = Edge(service=chromedriver)

driver.get('https://www.nix.ru/')

try:
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "#front_goods > div:nth-child(4321)")
            with open("data/nax_page.html", "w") as file:
                file.write(driver.page_source)
            break
        except Exception as e:
            del e
            html = driver.find_element(By.TAG_NAME, 'html')
            html.send_keys(Keys.PAGE_DOWN)
except Exception as e:
    print(e)
