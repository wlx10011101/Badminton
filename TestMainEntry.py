# coding=utf-8
'''
Created on 20190602

@author: WLX
'''
import sys
import unittest

from testcase.BookingCostTest import BookingCostTest
from testcase.BookingMessageTest import BookingMessageTest
from testcase.BookingSystemTest import BookingSystemTest
from testcase.BookingTimeTest import BookingTimeTest
from testcase.IntegrateTest import IntegrateTest


reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookingSystemTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookingMessageTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookingTimeTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IntegrateTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BookingCostTest))

    runner = unittest.TextTestRunner()
    runner.run(suite)
