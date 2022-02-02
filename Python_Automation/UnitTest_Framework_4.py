import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Test(unittest.TestCase):
    def testName(self):
        s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get('https://www.google.com/')
        titleOfWebPage = self.driver.title
        #self.assertEqual('Google123', titleOfWebPage, 'webpage title is not the same')
        self.assertNotEqual('Google123', titleOfWebPage)


if __name__ == '__main__':
    unittest.main()

