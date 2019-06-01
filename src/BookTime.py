# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''


# 对预定时间做预处理
# 需求设定羽毛球场从早上9点到晚上10点，且最小单位是为小时
# 我们将这13个小时是否被预定以01形式表示，即对每次预定时间段由13位的byte来表示
NO_BOOKED = "0"
BOOKED = "1"
BADMINTON_OPEN_HOUR = 9
BADMINTON_URATION_HOURS = 13


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
