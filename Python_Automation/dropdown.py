from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
driver = webdriver.Chrome(service=s)
#driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)

# select one option
drp = Select(driver.find_element(By.ID, 'RESULT_RadioButton-9'))
#drp.select_by_visible_text('Morning')
#drp.select_by_index(2)
drp.select_by_value('Radio-2')

# count how many options present
#capture all options from drop down and print them
print(len(drp.options))
all_options = drp.options
for option in all_options:
    print(option.text)




