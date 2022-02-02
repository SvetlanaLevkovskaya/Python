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
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
print(driver.title)

# 1. scroll down the page by pixel
#driver.execute_script('window.scrollBy(0,1000)', '')

# 2. scroll down till the element visible
#flag = driver.find_e nlement(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[25]/td[2]')
#driver.execute_script('arguments[0].scrollIntoView();', flag)

# 3. scroll down page till end
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
