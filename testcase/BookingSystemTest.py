# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
import unittest
from src.BookingSystem import BookingSystem


class Test(unittest.TestCase):

    def setUp(self):
        self.system = BookingSystem()

    def testInValidMessage(self):
        message = "abcdefghijklmnopqrst1234567890"
        response = self.system.start_booking(message)
        assert response == "Error: the booking is invalid!", \
            " Fail: " + str(response)

    def testValidMessageButTimeInvalid(self):
        message = "U001 2016-06-02 22:00~22:00 A"
        response = self.system.start_booking(message)
        assert response == "Error: the booking is invalid!", \
            " Fail: " + str(response)

    def testValidMessageAndAccepted(self):
        message = "U002 2017-08-01 19:00~22:00 A"
        response = self.system.start_booking(message)
        assert response == "Success: the booking is accepted!",\
            " Fail: " + str(response)

    def testValidMessageButConflict(self):
        message = "U002 2017-08-01 19:00~22:00 A"
        response = self.system.start_booking(message)
        assert response == "Success: the booking is accepted!",\
            " Fail: " + str(response)
        response = self.system.start_booking(message)
        assert response == "Error: the booking being cancelled does not exist!",\
            " Fail: " + str(response)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
