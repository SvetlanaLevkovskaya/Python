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
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

# #driver.find_element(By.XPATH, '//*[@id="txtUsername"]').send_keys('Admin')
# #driver.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys('admin123')
# driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()

switchTo = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
alert = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[1]/a')
windows = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[2]/a')
frames = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[3]/a')

actions = ActionChains(driver)

actions.move_to_element(switchTo).move_to_element(alert).move_to_element(windows).move_to_element(frames).click().perform()
