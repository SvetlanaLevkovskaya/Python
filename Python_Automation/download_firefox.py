from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


profile_path = r'D:\HW'
options = Options()
options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/pdf')
options.set_preference('browser.download.manager.showWhenStarting', False)
options.set_preference('browser.download.dir', profile_path)
options.set_preference('browser.download.folderList', 2)
options.set_preference('pdfjs.disabled', True)
service = Service(r'D:\HW\Python_Vadim_Course\geckodriver.exe')

driver = Firefox(service=service, options=options)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()


# download text file
driver.find_element(By.ID, 'textbox').send_keys('testing download text file')
driver.find_element(By.ID, 'createTxt').click() # generate file button
driver.find_element(By.ID,'link-to-download').click() # download link

# download pdf file
driver.find_element(By.ID,'pdfbox').send_keys('testing pdf')
driver.find_element(By.ID, 'createPdf').click() # generate file button
driver.find_element(By.ID,'pdf-link-to-download').click() # download link

driver.close()
