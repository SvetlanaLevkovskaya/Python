import unittest


def setUpModule(): # will be executed before executing any class or any method present in the test class
    print('setUpModule')


def tearDownModule(): # will be executed after completing everything present in the python module
    print('tearDownModule')


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):   # Execute before all test methods
        print('This is logging test')

    @classmethod
    def tearDown(self):    # Execute after all test methods
        print('This is logout test')

    @classmethod
    def setUpClass(cls):    # Execute once when the class started
        print('Open Application')

    @classmethod
    def tearDownClass(cls):        # Execute once when the class completed
        print('Close Application')

    def test_search(self):
        print('This is search test')

    def test_advansedsearch(self):
        print('This is Advansed search test')

    def test_prepaidRecharge(self):
        print('This is prepaid Recharge test')

    def test_posrpaidRecharge(self):
        print('This is postpaid Recharge test')


if __name__ == '__main__':
    unittest.main()
