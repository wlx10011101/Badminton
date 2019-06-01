# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
import datetime
import unittest

from src.BookTime import BookTime
from src.PriceHandler import PriceHandler


class PriceHandlerTest(unittest.TestCase):

    def testWeekendPrice1(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(9, 10)
        result = PriceHandler().totalCost(date, time)
        assert result == 40

    def testWeekendPrice2(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(11, 12)
        result = PriceHandler().totalCost(date, time)
        assert result == 40

    def testWeekendPrice3(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(12, 13)
        result = PriceHandler().totalCost(date, time)
        assert result == 50

    def testWeekendPrice4(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(17, 18)
        result = PriceHandler().totalCost(date, time)
        assert result == 50

    def testWeekendPrice5(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(18, 19)
        result = PriceHandler().totalCost(date, time)
        assert result == 60

    def testWeekendPrice6(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(21, 22)
        result = PriceHandler().totalCost(date, time)
        assert result == 60


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
