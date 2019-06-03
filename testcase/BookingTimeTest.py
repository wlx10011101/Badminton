# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
import unittest

from src.BookingTime import BookingTime


class BookingTimeTest(unittest.TestCase):

    def test9To22(self):
        result = BookingTime.convert_time_to_byte(9, 22)
        assert result == int("1111111111111", 2)

    def test10To10(self):
        result = BookingTime.convert_time_to_byte(10, 10)
        assert result == int("0000000000000", 2)

    def test9To10(self):
        result = BookingTime.convert_time_to_byte(9, 10)
        assert result == int("1000000000000", 2)

    def test9To12(self):
        result = BookingTime()
        print result.has_booking()


if __name__ == "__main__":
    unittest.main()
