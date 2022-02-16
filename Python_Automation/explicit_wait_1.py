from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://fh.by')
time.sleep(2)

present_page = driver.find_element(By.LINK_TEXT, 'Подарки').click()
time.sleep(2)

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable — it is Displayed and Enabled.
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present


wait = WebDriverWait(driver,10)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/aside/div/div/section[2]/div/button').click()
# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]
# /div/main/section/div/aside/div/div/section[2]/div/div[3]/label[7]/span'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, \
            '//*[@id="__next"]/div/main/section/div/aside/div/div/section[2]/div/div[2]/input'))).send_keys('BOSS')

wait.until(EC.element_to_be_clickable((By.XPATH, \
                '//*[@id="__next"]/div/main/section/div/aside/div/div/section[2]/div/div[3]/label/span'))).click()
