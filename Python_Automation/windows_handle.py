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
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
print(driver.current_window_handle) # CDwindow-4A83703FC89D10FA37B5D802CCDDDEEE - parent

handles = driver.window_handles # return all the handles values of open windows
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close() # close only parent browser

#driver.close()
#driver.quit() # close all windows
