from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)

btn = driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
time.sleep(5)

#driver.close() # currently focused browser
driver.quit() # closes all browsers
