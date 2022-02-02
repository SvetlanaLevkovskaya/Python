import DDT_def
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time


options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')


class TestExcel(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("http://demo.guru99.com/test/newtours/")
        self.driver.maximize_window()

        return self.driver

    def test_read_excel_file(self):

        path = 'D:\HW\Python_Vadim_Course\Login.xlsx'
        print(path.title())

        rows = DDT_def.getRowCount(path, 'Sheet1')

        for r in range(2, rows + 1):
            username = DDT_def.readData(path, "Sheet1", r, 1)
            password = DDT_def.readData(path, "Sheet1", r, 2)

            self.driver.find_element(By.NAME, "userName").clear()
            self.driver.find_element(By.NAME, "userName").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)

            self.driver.find_element(By.NAME, "submit").click()

            time.sleep(2)

            if self.driver.title == "Login: Mercury Tours":
                print("Test is passed!")
                DDT_def.writeData(path, "Sheet1", r, 3, "Test passed")
            else:
                print("Test failed")
                DDT_def.writeData(path, "Sheet1", r, 3, "Test failed")

            self.driver.back()
            # return self.driver


if __name__ == "__main__":
    unittest.main()
