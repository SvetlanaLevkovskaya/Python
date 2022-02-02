import unittest


class LogingTest(unittest.TestCase):
    def test_LoginByEmail(self):
        print('This is login by Email')
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print('This is login by Facebook')
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print('This is login by Twitter')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
