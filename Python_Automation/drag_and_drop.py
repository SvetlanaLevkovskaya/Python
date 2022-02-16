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
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
print(driver.title)

sourse_element = driver.find_element(By.XPATH, '//*[@id="box6"]')
target_element = driver.find_element(By.XPATH, '//*[@id="box106"]')

actions = ActionChains(driver)
actions.drag_and_drop(sourse_element, target_element).perform()
