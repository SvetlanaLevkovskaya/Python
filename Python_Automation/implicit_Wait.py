from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://www.agriculture.alberta.ca/app21/ldcalc")
driver.implicitly_wait(10)
assert 'Agriculture and Forestry : Applications & Tools - Crop' in driver.title

calc_page = driver.find_element(By.LINK_TEXT, 'Ammonia Losses from Liquid Manure Applications Calculator').click()
print(driver.title)
time.sleep(2)

driver.find_element(By.NAME, 'memo').send_keys('test')
driver.find_element(By.XPATH, '//*[@id="landSubmit"]').click()
