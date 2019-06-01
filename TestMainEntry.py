# coding=utf-8
'''
Created on 20190602

@author: WLX
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest

from testcase.BookingSystemTest import BookingSystemTest
from testcase.BookMessageTest import BookMessageTest
from testcase.BookTimeTest import BookTimeTest
from testcase.IntegrateTest import IntegrateTest
from testcase.PriceHandlerTest import PriceHandlerTest


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookingSystemTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookMessageTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookTimeTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IntegrateTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PriceHandlerTest))

    runner = unittest.TextTestRunner()
    runner.run(suite)
