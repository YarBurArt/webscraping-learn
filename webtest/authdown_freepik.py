from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import random
import time


chromedriver = EdgeService(EdgeChromiumDriverManager().install())
browser = Edge(service=chromedriver)


def slow_type(element, text) -> None:
    parts_text = [text[x:x+4] for x in range(0, len(text), 4)]
    for part in parts_text:
        time.sleep(random.choice([0.2, 0.5, 0.8]))
        element.send_keys(part)


def sing_in(login: str, password: str) -> None:
    browser.get('https://ru.freepik.com/')

    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "html"))
    )

    start_login_elem = browser.find_element(By.CLASS_NAME, "auth-link")
    assert "Войти" in start_login_elem.get_attribute("text")
    start_login_elem.click()

    email_login_elem = browser.find_element(By.CSS_SELECTOR,
                                            "#log-in > div.continue-with > button:nth-child(3)")
    email_login_elem.click()

    email = browser.find_element(
        By.CSS_SELECTOR,
        '#log-in > div.native-sign > form > div.form-item.form-item--email > label > input[type=text]'
    )
    paswd = browser.find_element(
        By.CSS_SELECTOR,
        '#log-in > div.native-sign > form > div.form-item.form-item--password > label > input[type=password]'
    )
    login_btt = browser.find_element(By.CSS_SELECTOR, '#submit')

    slow_type(email, login)
    slow_type(paswd, password)
    time.sleep(0.3)
    login_btt.click()


def download_url(url_link: str) -> None:
    browser.get(url_link)

    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "html"))
    )
    pre_download = browser.find_element(By.CSS_SELECTOR, '#download-file')
    pre_download.click()
    download = browser.find_element(
        By.CSS_SELECTOR,
        '#main > div > aside > div.detail__actions > div.detail__download > div.selection-download-wrapper > div > div > div.download-resource-container > div.popover.popover--bottom-right.noscript > button.download-button.button.button--md.button--green.button--fullwidth'
    )
    download.click()


if __name__ == "__main__":
    url_link = 'https://ru.freepik.com/free-photo/view-of-city-with-apartment-buildings-and-green-vegetation_43468051.htm#&position=7&from_view=collections'
    sing_in("example@email.com"
            "python~test_auth~down")
    download_url(url_link)
