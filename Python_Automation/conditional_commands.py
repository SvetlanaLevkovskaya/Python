from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
print(driver.title)

login_page = driver.find_element(By.LINK_TEXT, 'Sign In').click()
time.sleep(2)

user_name = driver.find_element(By.NAME, 'user')
print(user_name.is_displayed())
print(user_name.is_enabled())
time.sleep(2)

user_pass = driver.find_element(By.NAME, 'pass')
print(user_pass.is_displayed())
print(user_pass.is_enabled())
time.sleep(2)

user_name.send_keys('levkovskayase@gmail.com')
time.sleep(2)
user_pass.send_keys('12345678')
time.sleep(2)

singIn = driver.find_element(By.XPATH, '//*[@id="Login"]/button').click()


