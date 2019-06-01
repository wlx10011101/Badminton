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
        assert result == 40, "Fail: " + str(result)

    def testWeekendPrice2(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(11, 12)
        result = PriceHandler().totalCost(date, time)
        assert result == 40, "Fail: " + str(result)

    def testWeekendPrice3(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(12, 13)
        result = PriceHandler().totalCost(date, time)
        assert result == 50, "Fail: " + str(result)

    def testWeekendPrice4(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(17, 18)
        result = PriceHandler().totalCost(date, time)
        assert result == 50, "Fail: " + str(result)

    def testWeekendPrice5(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(18, 19)
        result = PriceHandler().totalCost(date, time)
        assert result == 60, "Fail: " + str(result)

    def testWeekendPrice6(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(21, 22)
        result = PriceHandler().totalCost(date, time)
        assert result == 60, "Fail: " + str(result)

    def testWeekendPrice7(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(11, 13)
        result = PriceHandler().totalCost(date, time)
        assert result == 90, "Fail: " + str(result)

    def testWeekendPrice8(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(17, 19)
        result = PriceHandler().totalCost(date, time)
        assert result == 110, "Fail: " + str(result)

    def testWeekdayPrice1(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(9, 10)
        result = PriceHandler().totalCost(date, time)
        assert result == 30, "Fail: " + str(result)

    def testWeekdayPrice2(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(11, 12)
        result = PriceHandler().totalCost(date, time)
        assert result == 30, "Fail: " + str(result)

    def testWeekdayPrice3(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(12, 13)
        result = PriceHandler().totalCost(date, time)
        assert result == 50, "Fail: " + str(result)

    def testWeekdayPrice4(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(17, 18)
        result = PriceHandler().totalCost(date, time)
        assert result == 50, "Fail: " + str(result)

    def testWeekdayPrice5(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(18, 19)
        result = PriceHandler().totalCost(date, time)
        assert result == 80, "Fail: " + str(result)

    def testWeekdayPrice6(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(19, 20)
        result = PriceHandler().totalCost(date, time)
        assert result == 80, "Fail: " + str(result)

    def testWeekdayPrice7(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookTime.convertTimeToByte(21, 22)
        result = PriceHandler().totalCost(date, time)
        assert result == 60, "Fail: " + str(result)

if __name__ == "__main__":
    unittest.main()
