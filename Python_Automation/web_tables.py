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
driver.maximize_window()
driver.get("file:///D:/HW/Python_Vadim_Course/Download%20Selenium%20Examples/code/websites/table.html")
print(driver.title)

rows = (len(driver.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr')))
columns = (len(driver.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr[1]/th')))
print(rows)
print(columns)

print('Fruits' + '    ' + 'Country')
for r in range(2, rows+1):
    for c in range(1, columns+1):
        value = driver.find_element(By.XPATH, '//*[@id="table"]/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(value, end ='    ')
    print()
