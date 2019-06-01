# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
from src.Config import BADMINTON_OPEN_HOUR, NO_BOOKED, BADMINTON_URATION_HOURS,\
    BOOKED

# 对预定时间做预处理


class BookTime(object):
    '''
    classdocs
    '''

    @staticmethod
    def convertTimeToByte(startHour, endHour):
        start = startHour - BADMINTON_OPEN_HOUR
        end = endHour - BADMINTON_OPEN_HOUR
        bookTimeByteList = [NO_BOOKED for _ in range(BADMINTON_URATION_HOURS)]
        for i in range(start, end):
            bookTimeByteList[i] = BOOKED
        bookTimeStr = "".join(bookTimeByteList)
        return int(bookTimeStr, 2)

    @staticmethod
    def noOneBook():
        return int("".join([NO_BOOKED for _ in range(BADMINTON_URATION_HOURS)]), 2)

    @staticmethod
    def isOpen(bookTime):
        return BADMINTON_OPEN_HOUR <= int(bookTime) <= BADMINTON_OPEN_HOUR + BADMINTON_URATION_HOURS
