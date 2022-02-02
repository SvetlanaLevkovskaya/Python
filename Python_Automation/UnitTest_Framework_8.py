import unittest


class Test(unittest.TestCase):
    def testName(self):
        self.assertGreater(100, 10)

    def testName1(self):
        self.assertGreaterEqual(100, 100)

    def testName2(self):
        self.assertLess(1000, 10000)

    def testName3(self):
        self.assertLessEqual(100000, 10000)


if __name__ == '__main__':
    unittest.main()
