# coding=utf-8
'''
Created on 2019年6月1日

@author: --
'''
import unittest

from src.BookingMessage import BookingMessage


class BookingMessageTest(unittest.TestCase):

    def test_message_valid1(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:00~22:00", "A")
        assert bookMessage.isValid == False

    def test_message_valid2(self):
        bookMessage = BookingMessage('U01101', "2016-06-31", "22:00~22:00", "A")
        assert bookMessage.isValid == False

    def test_message_valid3(self):
        bookMessage = BookingMessage('U01101', "2016-06-01", "22:00~12:00", "A")
        assert bookMessage.isValid == False

    def test_message_valid4(self):
        bookMessage = BookingMessage('U01101', "2016-06-01", "21:00~22:00", "A")
        assert bookMessage.isValid == True

    def test_message_valid5(self):
        bookMessage = BookingMessage(
            'U01101', "2016-06-01", "21:00~22:00", "A", "C")
        assert bookMessage.isValid == True

    def test_message_valid6(self):
        bookMessage = BookingMessage(
            'U01101', "2016-06-01", "22:00~22:00", "A", "D")
        assert bookMessage.isValid == False

    def test_message_valid7(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:~22:00", "A")
        assert bookMessage.isValid == False

    def test_message_valid8(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:00~22:30", "A")
        assert bookMessage.isValid == False

    def test_message_valid9(self):
        bookMessage = BookingMessage('U01101', "2016-06-02", "22:00-22:30", "A")
        assert bookMessage.isValid == False


if __name__ == "__main__":
    unittest.main()
