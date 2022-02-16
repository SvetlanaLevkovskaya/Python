from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
print(driver.title)

element = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
actions = ActionChains(driver)
actions.double_click(element).perform()
