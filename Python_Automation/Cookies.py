from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

s = Service('D:\HW\Python_Vadim_Course\chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/")
driver.maximize_window()
print(driver.title)

# Capture all cookies from browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Adding new cookies
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Deleting specific cookies by using name of cookie
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# deleting all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Count number of cookies
# Read Cookies pairs
