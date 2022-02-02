from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
#driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)


driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)

# closes alert window using OK button
#driver.switch_to_alert().accept()

# try:
#     WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
#     alert = driver.switch_to.alert
#     alert.accept()
#     print("alert accepted")
# except TimeoutException:
#     print("no alert")

# closes alert window using Cancel button
#driver.switch_to_alert().dismiss()
try:
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
    alert = driver.switch_to.alert
    alert.dismiss()
    print("alert dismissed")
except TimeoutException:
    print("no alert")
