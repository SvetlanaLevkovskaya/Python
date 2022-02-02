from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

# s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window()
# print(driver.title)
#
# element = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')
# actions = ActionChains(driver)
# actions.context_click(element).perform()

username = 'admin@yourstore.com'
password = 'admin'


s = Service('D:/HW/Python_Vadim_Course/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://admin-demo.nopcommerce.com/')
# lp = LoginPage1(self.driver)
driver.find_element(By.ID, 'Email').clear()
driver.find_element(By.ID, 'Email').send_keys(username)
driver.find_element(By.ID, 'Password').clear()
driver.find_element(By.ID, 'Password').send_keys(password)
driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
act_title = driver.title
if act_title == 'Dashboard / nopCommerce administration':
    print(act_title)
else:
    print("This is wrong")
