from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# The above is a simplification for installing the driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
# The above it's for web element identification, wait conditions, and wait times
import random
import time
import re

# Create a service object for the EdgeDriver and setup core driver object
chromedriver = EdgeService(EdgeChromiumDriverManager().install())
browser = Edge(service=chromedriver)


def isvalid_email(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return bool(re.fullmatch(regex, email))


def isvalid_url(url: str) -> bool:
    regex = re.compile(r'^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.'
                       r'[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$')
    return bool(re.fullmatch(regex, url))


def slow_type(element, text) -> None:
    """
    Simulates slow typing by splitting the text into 4-character chunks
    and pausing for a random amount of time between each chunk
    :param element: where to enter text
    :param text: what to enter
    """
    parts_text = [text[part:part+4] for part in range(0, len(text), 4)]
    for part in parts_text:
        time.sleep(random.choice([0.2, 0.5, 0.8]))
        element.send_keys(part)


def sing_in(login_email_user: str, password_user: str) -> WebElement | None:
    """
    Log in to the Freepik website using the specified login email and password.
    :param login_email_user: login in the form of mail
    :param password_user: password of 6 - 60 characters (restriction from this site)
    :return: WebElement avatar image if all good
    """
    assert isvalid_email(login_email_user) and login_email_user != password_user, "Invalid login or password"

    # launching the browser and waiting for the page to load fully
    start_url = 'https://ru.freepik.com/'
    browser.get(start_url)
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "html"))
    )
    # get to the login form
    start_login_elem = browser.find_element(By.CLASS_NAME, "auth-link")
    assert "Войти" in start_login_elem.get_attribute("text")
    start_login_elem.click()
    # get to the login form again
    email_login_elem = browser.find_element(
        By.CSS_SELECTOR,
        "#log-in > div.continue-with > button:nth-child(3)")
    email_login_elem.click()
    # find password and login fields by css selector
    email = browser.find_element(
        By.CSS_SELECTOR,
        '#log-in > div.native-sign > form > div.form-item.form-item--email > label > input[type=text]'
    )
    paswd = browser.find_element(
        By.CSS_SELECTOR,
        '#log-in > div.native-sign > form > div.form-item.form-item--password > label > input[type=password]'
    )
    login_btt = browser.find_element(By.CSS_SELECTOR, '#submit')
    # human-simulated input
    slow_type(email, login_email_user)
    slow_type(paswd, password_user)
    time.sleep(0.3)
    login_btt.click()

    # if everything is fine, then we throw out the avatar
    if browser.current_url == start_url:
        return browser.find_element(
            By.CSS_SELECTOR,
            "#navigation > div > div > div.gr-auth.gr-auth--logged.gr-auth--not-premium.gr-auth--not-essential > "
            "div.gr-auth__connected > div > div.popover.popover--mobile-fullscreen.popover--bottom-right.popover--width"
            "-xs.block.gr-auth__popover.gr-auth__popover--new-home > button > div "
            "> span.avatar.avatar--xs.avatar--circle > img")


def download_url(url_img: str) -> None:
    """
    Downloading the image from the link, use only after logging in to the account on the site
    :param url_img: the url of the page image on the site, is not a direct link to the image by api
    """
    assert isvalid_url(url_img), f"Invalid url: {url_img}"

    # launching the browser and waiting for the page to load fully
    browser.get(url_img)
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "html"))
    )
    # find the download button and the button below it, then click
    pre_download = browser.find_element(By.CSS_SELECTOR, '#download-file')
    pre_download.click()
    download = browser.find_element(
        By.CSS_SELECTOR,
        '#main > div > aside > div.detail__actions > div.detail__download > div.selection-download-wrapper > div > div '
        '> div.download-resource-container > div.popover.popover--bottom-right.noscript > '
        'button.download-button.button.button--md.button--green.button--fullwidth'
    )
    download.click()


if __name__ == "__main__":
    url_link = 'https://ru.freepik.com/free-photo/view-of-city-with-apartment-' \
               'buildings-and-green-vegetation_43468051.htm#&position=7&from_view=collections'
    sing_in("example@email.com",
            "python~test_auth~down")
    download_url(url_link)
