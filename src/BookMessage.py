# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
import datetime
from src.BookTime import BookTime
MESSAGE_INVALID = -1
MESSAGE_VALID = 1


class BookMessage(object):
    '''
    classdocs
    '''

    def __init__(self, username, bookDate, bookDuration, bookArea, cancle=None):
        '''
        Constructor
        '''
        self.isValid = True
        self.user = username
        self.bookDate = self._format_date(bookDate)
        self.bookTime = self._format_time(bookDuration)
        self.bookArea = bookArea
        self.isCancle = self._format_cancle(cancle)
        self.cost = self._calc_cost()

    def _format_date(self, dateStr):
        try:
            return datetime.datetime.strptime(dateStr, "%Y-%m-%d")
        except Exception as e:
            self.isValid = False
            return None

    def _format_time(self, timeStr):
        timeList = timeStr.split("~")
        if len(timeList) != 2:
            self.isValid = False
            return None
        hourList = []
        for item in timeList:
            timeSplit = item.split(":")
            if len(timeList) != 2 or timeSplit[1] != "00" or not BookTime.isOpen(timeSplit[0]):
                self.isValid = False
                return None
            else:
                hourList.append(int(timeSplit[0]))
        if hourList[1] < hourList[0]:
            self.isValid = False
            return None
        result = BookTime.convertTimeToByte(hourList[0], hourList[1])
        if result <= 0:
            self.isValid = False
            return None
        else:
            return result

    def _format_cancle(self, cancleStr):
        if cancleStr != None:
            if cancleStr == "C":
                return True
            else:
                self.isValid = False
        else:
            return False

    def _calc_cost(self):
        if self.isValid:
            pass
        else:
            return 0

    def _is_weekent(self):
        pass
