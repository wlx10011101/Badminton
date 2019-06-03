# coding=utf-8
'''
Created on 2019年6月1日

@author: --
'''
import unittest

from src.BookingMessage import BookingMessage


class BookingMessageTest(unittest.TestCase):

    def testMessageValid1(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:00~22:00", "A")
        assert bookMessage.isValid == False

    def testMessageValid2(self):
        bookMessage = BookingMessage('U01101', "2016-06-31", "22:00~22:00", "A")
        assert bookMessage.isValid == False

    def testMessageValid3(self):
        bookMessage = BookingMessage('U01101', "2016-06-01", "22:00~12:00", "A")
        assert bookMessage.isValid == False

    def testMessageValid4(self):
        bookMessage = BookingMessage('U01101', "2016-06-01", "21:00~22:00", "A")
        assert bookMessage.isValid == True

    def testMessageValid5(self):
        bookMessage = BookingMessage(
            'U01101', "2016-06-01", "21:00~22:00", "A", "C")
        assert bookMessage.isValid == True

    def testMessageValid6(self):
        bookMessage = BookingMessage(
            'U01101', "2016-06-01", "22:00~22:00", "A", "D")
        assert bookMessage.isValid == False

    def testMessageValid7(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:~22:00", "A")
        assert bookMessage.isValid == False

    def testMessageValid8(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:00~22:30", "A")
        assert bookMessage.isValid == False

    def testMessageValid9(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:00-22:30", "A")
        assert bookMessage.isValid == False


if __name__ == "__main__":
    unittest.main()
