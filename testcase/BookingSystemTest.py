# coding=utf-8
'''
Created on 20190601

@author: --
'''
import unittest
from src.BookingSystem import BookingSystem
from src.Config import BOOKING_RESPONSE_DEFINE, BOOKING_CONFLICT,\
    BOOKING_SUCCESS, BOOKING_INVALID, CANCEL_NOT_EXIST


class BookingSystemTest(unittest.TestCase):

    def setUp(self):
        self.system = BookingSystem()

    def test_invalid_message(self):
        message = "abcdefghijklmnopqrst1234567890"
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID), \
            " Fail: " + str(response)

    def test_vlid_message_but_time_invalid(self):
        message = "U001 2016-06-02 22:00~22:00 A"
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID), \
            " Fail: " + str(response)

    def test_valid_message_and_accepted(self):
        message = "U002 2017-08-01 19:00~22:00 A"
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)

    def test_valid_message_but_conflict(self):
        message = "U002 2017-08-01 19:00~22:00 A"
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_CONFLICT),\
            " Fail: " + str(response)

    def test_two_valid_message(self):
        message1 = "U002 2017-08-01 15:00~18:00 A"
        message2 = "U002 2017-08-01 18:00~22:00 A"
        response = self.system.start_booking(message1)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)
        response = self.system.start_booking(message2)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)

    def test_invalid_cancel_message1(self):
        message = "U002 2017-08-01 19:00~22:00 A D"
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID),\
            " Fail: " + str(response)

    def test_valid_cancel_message1_but_not_exist(self):
        message = "U002 2017-08-01 19:00~22:00 A C"
        response = self.system.start_booking(message)
        assert response == BOOKING_RESPONSE_DEFINE.get(CANCEL_NOT_EXIST),\
            " Fail: " + str(response)

    def test_book_success_but_Cancel_not_exit(self):
        message1 = "U002 2017-08-01 19:00~22:00 A"
        message2 = "U002 2017-08-11 19:00~22:00 A C"
        response = self.system.start_booking(message1)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)
        response = self.system.start_booking(message2)
        assert response == BOOKING_RESPONSE_DEFINE.get(CANCEL_NOT_EXIST),\
            " Fail: " + str(response)

    def test_book_success_and_cancel_success(self):
        message1 = "U002 2017-08-01 19:00~22:00 A"
        message2 = "U002 2017-08-01 19:00~22:00 A C"
        response = self.system.start_booking(message1)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)
        response = self.system.start_booking(message2)
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS),\
            " Fail: " + str(response)


if __name__ == "__main__":
    unittest.main()
