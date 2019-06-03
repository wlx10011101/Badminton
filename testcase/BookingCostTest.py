# coding=utf-8
'''
Created on 20190601

@author: --
'''
import datetime
import unittest

from src.BookingCost import BookingCost
from src.BookingTime import BookingTime


class BookingCostTest(unittest.TestCase):

    def testWeekendPrice1(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((9, 10))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 40, "Fail: " + str(result)

    def testWeekendPrice2(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((11, 12))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 40, "Fail: " + str(result)

    def testWeekendPrice3(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((12, 13))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 50, "Fail: " + str(result)

    def testWeekendPrice4(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((17, 18))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 50, "Fail: " + str(result)

    def testWeekendPrice5(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((18, 19))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 60, "Fail: " + str(result)

    def testWeekendPrice6(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((21, 22))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 60, "Fail: " + str(result)

    def testWeekendPrice7(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((11, 13))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 90, "Fail: " + str(result)

    def testWeekendPrice8(self):
        date = datetime.datetime.strptime("2019-06-01", "%Y-%m-%d")
        time = BookingTime((17, 19))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 110, "Fail: " + str(result)

    def testWeekdayPrice1(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((9, 10))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 30, "Fail: " + str(result)

    def testWeekdayPrice2(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((11, 12))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 30, "Fail: " + str(result)

    def testWeekdayPrice3(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((12, 13))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 50, "Fail: " + str(result)

    def testWeekdayPrice4(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((17, 18))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 50, "Fail: " + str(result)

    def testWeekdayPrice5(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((18, 19))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 80, "Fail: " + str(result)

    def testWeekdayPrice6(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((19, 20))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 80, "Fail: " + str(result)

    def testWeekdayPrice7(self):
        date = datetime.datetime.strptime("2019-05-31", "%Y-%m-%d")
        time = BookingTime((21, 22))
        bookingCost = BookingCost(date, time)
        result = bookingCost.cost
        assert result == 60, "Fail: " + str(result)


if __name__ == "__main__":
    unittest.main()
