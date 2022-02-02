from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

s = Service('D:\HW\Python_Vadim_Course\chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()
print(driver.title)

#driver.save_screenshot("D:\HW\Python_Vadim_Course\homepage.png")
#driver.get_screenshot_as_file("D:\HW\Python_Vadim_Course\homepage1.jpg")
driver.get_screenshot_as_file("D:\HW\Python_Vadim_Course\homepage1.png")
