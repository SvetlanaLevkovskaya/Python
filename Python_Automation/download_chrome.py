from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": r"D:\HW"})

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
print(driver.title)

# # download text file
# driver.find_element(By.ID, 'textbox').send_keys('testing download text file')
# driver.find_element(By.ID, 'createTxt').click() # generate file button
# driver.find_element(By.ID,'link-to-download').click() # download link
#
# # download pdf file
# driver.find_element(By.ID,'pdfbox').send_keys('testing pdf')
# driver.find_element(By.ID, 'createPdf').click() # generate file button
# driver.find_element(By.ID,'pdf-link-to-download').click() # download link


# download text file
driver.find_element(By.ID, 'textbox').send_keys('testing download text file')
driver.find_element(By.ID, 'createTxt').click() # generate file button
driver.find_element(By.ID,'link-to-download').click() # download link

# download pdf file
driver.find_element(By.ID,'pdfbox').send_keys('testing pdf')
driver.find_element(By.ID, 'createPdf').click() # generate file button
driver.find_element(By.ID,'pdf-link-to-download').click() # download link


time.sleep(2)
driver.close()
