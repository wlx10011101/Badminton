# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
from src.Config import BADMINTON_OPEN_HOUR, NO_BOOKED, BADMINTON_URATION_HOURS,\
    BOOKED, BINARY, FIRST, SECOND


class BookingTime(object):
    '''
    对预定时间做预处理，根据羽毛球馆营业13个小时，以13位byte来表示是否被预约
    '''

    def __init__(self, hourTuple=None):
        self.time = self.convert_time_to_byte(hourTuple[FIRST], hourTuple[SECOND]) if hourTuple else self.new_booking_time()

    @staticmethod
    def convert_time_to_byte(startHour, endHour):
        start = startHour - BADMINTON_OPEN_HOUR
        end = endHour - BADMINTON_OPEN_HOUR
        bookTimeByteList = [NO_BOOKED for _ in range(BADMINTON_URATION_HOURS)]
        for i in range(start, end):
            bookTimeByteList[i] = BOOKED
        bookTimeStr = "".join(bookTimeByteList)
        return int(bookTimeStr, BINARY)

    @staticmethod
    def new_booking_time():
        return int("".join([NO_BOOKED for _ in range(BADMINTON_URATION_HOURS)]), BINARY)

    @staticmethod
    def is_open(whichHour):
        return BADMINTON_OPEN_HOUR <= int(whichHour) <= BADMINTON_OPEN_HOUR + BADMINTON_URATION_HOURS

    def is_conflict(self, bookingTime):
        return self.time & bookingTime.time

    def add(self, bookingTime):
        self.time = self.time | bookingTime.time
        return self

    def contain(self, whichHour):
        return self.time & whichHour

    def cut(self, bookingTime):
        self.time = self.time & (~ bookingTime.time)
        return self

    def has_booking(self):
        return self.time > self.new_booking_time()
