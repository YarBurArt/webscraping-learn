from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
# test: selenium is work? and mini cheatsheet


profile_path = r'C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\1793b34j.default'
options = Options()
options.set_preference('profile', profile_path)
service = Service(r'D:\\geckodriverFrifox')

driver = webdriver.Firefox(service=service, options=options)


driver.get("http://www.python.org")
assert "Python" in driver.title  # try
elem = driver.find_element("name", "q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
