from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service('D:\HW\Python_Vadim_Course\chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.maximize_window()
print(driver.title)
driver.find_element(By.LINK_TEXT, 'FRAMES').click()

driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()
# driver.implicitly_wait(10)
time.sleep(3)
driver.switch_to.parent_frame()

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT, 'WebDriver').click()
# driver.implicitly_wait(10)
# driver.switch_to_default_content()
time.sleep(3)
driver.switch_to.parent_frame()

driver.switch_to.frame('classFrame')
time.sleep(3)
# driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/div[1]/ul/li[6]').click()
