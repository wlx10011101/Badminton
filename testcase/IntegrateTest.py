# coding=utf-8
'''
Created on 20190611

@author: WLX
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest

from src.BookingSystem import BookingSystem
from src.Config import BOOKING_RESPONSE_DEFINE, BOOKING_INVALID, BOOKING_SUCCESS,\
    BOOKING_CONFLICT, CANCEL_NOT_EXIST


class IntegrateTest(unittest.TestCase):

    def setUp(self):
        self.system = BookingSystem()

    def testCase1FromProject(self):
        print "---------------testCase1FromProject--------------------"
        message1 = "abcdefghijklmnopqrst1234567890"
        message2 = "U001 2016-06-02 22:00~22:00 A"
        message3 = "U002 2017-08-01 19:00~22:00 A"
        message4 = "U003 2017-08-02 13:00~17:00 B"
        message5 = "U004 2017-08-03 15:00~16:00 C"
        message6 = "U005 2017-08-05 09:00~11:00 D"
        totalExpect = ["收入汇总", "---",
                       "场地:A", "2017-08-01 19:00~22:00 200 元", "小计：200 元", "",
                       "场地:B", "2017-08-02 13:00~17:00 200 元", "小计：200 元", "",
                       "场地:C", "2017-08-03 15:00~16:00 50 元", "小计：50 元", "",
                       "场地:D", "2017-08-05 09:00~11:00 80 元", "小计：80 元", "---",
                       "总计：530 元"]
        response = self.system.start_booking(message1)
        print message1
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID)
        response = self.system.start_booking(message2)
        print message2
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID)
        response = self.system.start_booking(message3)
        print message3
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        response = self.system.start_booking(message4)
        print message4
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        response = self.system.start_booking(message5)
        print message5
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        response = self.system.start_booking(message6)
        print message6
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        print ""
        response = self.system.get_subtotal()
        for i in range(len(response)):
            print "> " + response[i].encode("gb2312")
            assert response[i] == totalExpect[i], "Expect: " + totalExpect[i] + " , But Get: " + response[i]

    def testCase2FromProject(self):
        print "---------------testCase2FromProject--------------------"
        message1 = "U002 2017-08-01 19:00~22:00 A"
        message2 = "U003 2017-08-01 18:00~20:00 A"
        message3 = "U002 2017-08-01 19:00~22:00 A C"
        message4 = "U002 2017-08-01 19:00~22:00 A C"
        message5 = "U003 2017-08-01 18:00~20:00 A"
        message6 = "U003 2017-08-02 13:00~17:00 B"
        totalExpect = ["收入汇总", "---",
                       "场地:A", "2017-08-01 18:00~20:00 160 元",
                       "2017-08-01 19:00~22:00 违约金 100 元", "小计：260 元", "",
                       "场地:B", "2017-08-02 13:00~17:00 200 元", "小计：200 元", "",
                       "场地:C", "小计：0 元", "", "场地:D", "小计：0 元",
                       "---", "总计：460 元"]
        print message1
        response = self.system.start_booking(message1)
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        print message2
        response = self.system.start_booking(message2)
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_CONFLICT)
        print message3
        response = self.system.start_booking(message3)
        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        print message4
        response = self.system.start_booking(message4)

        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(CANCEL_NOT_EXIST)
        print message5
        response = self.system.start_booking(message5)

        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        print message6
        response = self.system.start_booking(message6)

        print "> " + response
        assert response == BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        print ""
        response = self.system.get_subtotal()
        for i in range(len(response)):
            print "> " + response[i].encode("gb2312")
            assert response[i] == totalExpect[i], "Expect: " + totalExpect[i] + " , But Get: " + response[i]

if __name__ == "__main__":
    unittest.main()
