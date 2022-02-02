from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)

# How to find how many input boxes present in the webpage
input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(input_boxes))


# How to get the status
status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print(status)
status1 = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print(status1)


# How to provide the value into text box
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('pavan')
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('kumar')
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys('3333333333333')

