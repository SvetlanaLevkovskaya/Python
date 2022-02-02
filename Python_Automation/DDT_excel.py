import DDT_def
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time


s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path = 'D:\HW\Python_Vadim_Course\Login.xlsx'
print(path.title())
rows = DDT_def.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = DDT_def.readData(path, 'Sheet1', r, 1)
    password = DDT_def.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.NAME, "userName").clear()
    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    time.sleep(2)

    if driver.title == 'Login: Mercury Tours':
        print('test is passed')
        DDT_def.writeData(path, 'Sheet1', r, 3, 'test passed')
    else:
        print('test failed')
        DDT_def.writeData(path, 'Sheet1', r, 3, 'test failed')

    driver.back()


    # driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]').click()


