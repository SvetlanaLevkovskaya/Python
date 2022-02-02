from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://www.agriculture.alberta.ca/app21/ldcalc")
print(driver.title)
time.sleep(2)

calc_page = driver.find_element(By.LINK_TEXT, 'Ammonia Losses from Liquid Manure Applications Calculator').click()
print(driver.title)
time.sleep(2)

Dry_radio = driver.find_element(By.CSS_SELECTOR, "#soilMoistureDry")
print('status of Dry radio button =',  Dry_radio.is_selected())

Wet_radio = driver.find_element(By.CSS_SELECTOR, "#soilMoistureWet")
print('status of Wet radio button =', Wet_radio.is_selected())
