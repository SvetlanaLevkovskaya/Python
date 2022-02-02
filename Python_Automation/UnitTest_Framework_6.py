import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Test(unittest.TestCase):
    def testName(self):
        s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        #self.driver = None
        #self.driver.get('https://www.google.com/')
        #titleOfWebPage = self.driver.title
        #self.assertIsNone(self.driver)
        self.assertIsNotNone(self.driver)


if __name__ == '__main__':
    unittest.main()
