from selenium import webdriver
# sample authorization test 

chromedriver = "H:\\code\\python\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('https://example.com/login/')

email = browser.find_element_by_id('email')
password = browser.find_element_by_id('password')
login = browser.find_element_by_id('submit')

email.send_keys('my_mail')
password.send_keys('my_pass')
login.click()
