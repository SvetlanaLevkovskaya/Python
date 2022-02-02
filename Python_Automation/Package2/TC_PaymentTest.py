import unittest


class PaymentTest(unittest.TestCase):
    def test_PaymentInDollar(self):
        print('This is payment in dollar test')
        self.assertTrue(True)

    def test_PaymentInRubles(self):
        print('This is payment in rubles test')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
