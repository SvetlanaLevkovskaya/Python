from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
#driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)

# Working with radiobuttons
# Selected or not isSelected()
status = driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print(status)

# Selecting raido button
# Select male
driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label').click()

status = driver.find_element(By.ID, 'RESULT_RadioButton-7_0').is_selected()
print(status)

# Selecting check box
# Select sunday
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()

# Select monday
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[2]/td/label').click()

# Click
