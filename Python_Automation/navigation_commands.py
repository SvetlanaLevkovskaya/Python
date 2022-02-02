from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)


driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)

time.sleep(5)
driver.back()
print(driver.title)

time.sleep(5)
driver.forward()
print(driver.title)

driver.close()
