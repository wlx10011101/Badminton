# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
import datetime
import time

from src.BookTime import BookTime
from src.PriceHandler import PriceHandler


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
        self.noCancelCost = PriceHandler().totalCost(self.bookDate, self.bookTime) if self.isValid else 0
        self.cost = PriceHandler().totalCost(self.bookDate, self.bookTime, self.isCancle) if self.isValid else 0

    def __str__(self):
        startHourStr = time.strftime("%H:%M", time.strptime(str(self.startHour) + ":00", "%H:%M"))
        endHourStr = time.strftime("%H:%M", time.strptime(str(self.endHour) + ":00", "%H:%M"))
        returnStr = self.bookDate.strftime("%Y-%m-%d") + " " + startHourStr + "~" + endHourStr + " "
        if self.isCancle:
            returnStr += "违约金 " + str(self.cost) + " 元"
        else:
            returnStr += str(self.cost) + " 元"
        return returnStr

    def __cmp__(self, s):
        if self.bookDate < s.bookDate:
            return -1
        elif self.bookDate > s.bookDate:
            return 1
        else:
            #             if self.startHour == s.startHour and self.endHour == s.endHour:
            #                 if self.isCancle == self.isCancle:
            #                     return 0
            #                 elif self.isCancle is True:
            #                     return -1
            #                 else:
            #                     return 1
            if self.startHour < s.startHour:
                return -1
            else:
                return 1

    def __eq__(self, bookMessage):
        attrNames = ["user", "bookDate", "bookTime", "bookArea"]
        isEqual = True
        if bookMessage.isCancle:
            isEqual = False
        for item in attrNames:
            if not (hasattr(self, item) and hasattr(bookMessage, item)
                    and getattr(self, item) == getattr(bookMessage, item)):
                isEqual = False
        return isEqual

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
        self.startHour = hourList[0]
        self.endHour = hourList[1]
        result = BookTime.convertTimeToByte(self.startHour, self.endHour)
        if result <= 0:
            self.isValid = False
            return None
        else:
            return result

    def _format_cancle(self, cancleStr):
        if cancleStr is not None:
            if cancleStr == "C":
                return True
            else:
                self.isValid = False
        else:
            return False

    def _calc_cost(self):
        return PriceHandler().totalCost(self.bookDate, self.bookTime, self.isCancle)
