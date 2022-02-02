import unittest
from Package1.TC_LoginTest import LogingTest
from Package1.TC_SignUpTest import SignUpTest
from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnTest import PaymentReturnTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LogingTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# creating test suits
sanityTestSuit = unittest.TestSuite([tc1, tc2])
functionalTestSuit = unittest.TestSuite([tc3, tc4])
masterTestSuit = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuit)

