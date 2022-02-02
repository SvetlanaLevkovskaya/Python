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


driver.switch_to.frame('frame-one1434677811')

driver.find_element(By.ID, 'RESULT_FileUpload-10').send_keys('D:\HW\english\passive-voice_56903.doc')