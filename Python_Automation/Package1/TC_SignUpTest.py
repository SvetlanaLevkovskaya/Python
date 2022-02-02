import unittest


class SignUpTest(unittest.TestCase):
    def test_SignUpByEmail(self):
        print('This is sign up by Email')
        self.assertTrue(True)

    def test_SignUpByFacebook(self):
        print('This is sign up by Facebook')
        self.assertTrue(True)

    def test_SignUpByTwitter(self):
        print('This is sign up by Twitter')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
