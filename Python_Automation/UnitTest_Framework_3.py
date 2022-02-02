import unittest


class AppTesting(unittest.TestCase):
    @unittest.SkipTest    # decorator
    def test_search(self):
        print('This is search test')

    @unittest.skip('I am skipping this skip method because it is not ready yet')
    def test_advancedsearch(self):
        print('This is Advanced search test')

    @unittest.skipIf(1 == 1, 'number are not equal')
    def test_prepaidRecharge(self):
        print('This is prepaid Recharge test')

    def test_posrpaidRecharge(self):
        print('This is postpaid Recharge test')

    def test_loginbygmail(self):
        print('This is login by email')

    def test_loginbetwitter(self):
        print('This is login by twitter')


if __name__ == '__main__':
    unittest.main()
