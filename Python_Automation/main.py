from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get("http://newtours.demoaut.com/")
# print(driver.title)


s = Service('D:\HW\Python_Vadim_Course\geckodriver.exe')
driver = webdriver.Firefox(service=s)
driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
print(driver.page_source)
driver.close()
