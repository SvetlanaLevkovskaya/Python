from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
#driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)

# how many links present
links = driver.find_elements(By.TAG_NAME, 'a')
print('Number of links =', len(links))

# capture links
for link in links:
    print(link.text)

# click on the links
driver.find_element(By.PARTIAL_LINK_TEXT, 'REG').click()