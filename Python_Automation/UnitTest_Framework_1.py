import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SearchEnginesTest(unittest.TestCase):

    def setUp(self):
        s = Service('D:\HW\Python_Vadim_Course\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        #self.driver.implicitly_wait(10)
        # self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

        return self.driver

    def test_Google(self):
        # s = Service('D:\HW\Python_Vadim_Course\chromedriver')
        # self.driver = webdriver.Chrome(service=s)
        # self.driver.implicitly_wait(10)
        self.driver.get('https://www.google.com/')
        print('Title of the page is: ' + self.driver.title)

    def test_Bing(self):
        # s = Service('D:\HW\Python_Vadim_Course\chromedriver')
        # self.driver = webdriver.Chrome(service=s)
        # self.driver.implicitly_wait(10)
        self.driver.get('https://www.bing.com/')
        print('Title of the page is: ' + self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
