from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com/")

flight_page = driver.find_element(By.XPATH, '//*[@id="wizardMainRegionV2"]/div/div/div/div/ul/li[2]/a/span').click()
time.sleep(2)

flight_on = driver.find_element(By.XPATH, '//*[@id="location-field-leg1-origin-menu"]/div[1]/div[1]/button').click()
flight_where = driver.find_element(By.XPATH, '//*[@id="location-field-leg1-origin"]').send_keys('SFO')
flight_where_search = driver.find_element(By.XPATH, \
                            '//*[@id="location-field-leg1-origin-menu"]/div[2]/div[2]/ul/li[6]/button/div').click()
print(flight_where_search)
time.sleep(2)

flight_to = driver.find_element(By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[1]/div[1]/button').click()
flight_to_2 = driver.find_element(By.XPATH, '//*[@id="location-field-leg1-destination"]').send_keys('NYC')
flight_to_search = driver.find_element(By.XPATH, \
                                '//*[@id="location-field-leg1-destination-menu"]/div[2]/div[2]/ul/li[6]/button').click()
print(flight_to_search)
time.sleep(2)

# driver.find_element(By.ID, 'd1-btn').clear()
data_0 = driver.find_element(By.XPATH, '//*[@id="d1-btn"]').click()
time.sleep(2)
# data_1 = driver.find_element(By.XPATH, '
# //*[@id="wizard-flight-tab-roundtrip"]
# /div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[5]/button').click()
data_1_1 = driver.find_element(By.XPATH, \
            '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[3]/button').click()
# print(data_1)
time.sleep(2)

data_2 = driver.find_element(By.XPATH, '//*[@id="d2-btn"]').click()
time.sleep(2)
# data_1 = driver.find_element(By.XPATH,
# '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]
# /div/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[5]/button').click()
data_2_1 = driver.find_element(By.XPATH, \
            '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/button').click()
# print(data_1)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()
time.sleep(2)
