# coding=utf-8
'''
Created on 20190601

@author: --
'''
import datetime
import time

from src.BookingCost import BookingCost
from src.BookingTime import BookingTime
from src.Config import FIRST, SECOND, ERROR


class BookingMessage(object):
    '''
    预定消息处理，判断消息是否正确，并格式化，先行计算消费金额
    '''

    def __init__(self, username, bookingDate, bookingDuration, bookingArea, cancle=None):
        '''
        Constructor
        '''
        self.isValid = True
        self.startHour = None
        self.endHour = None
        self.user = username
        self.date = self._format_date(bookingDate)
        self.time = self._format_time(bookingDuration)
        self.area = bookingArea
        self.isCancle = self._format_cancle(cancle)
        self._bookingCost = BookingCost(self.date, self.time, self.isCancle) if self.isValid else None

    @property
    def income(self):
        if self._bookingCost:
            return self._bookingCost.income
        else:
            return 0

    @property
    def cost(self):
        if self._bookingCost:
            return self._bookingCost.cost
        else:
            return 0

    def __str__(self):
        startHourStr = time.strftime("%H:%M", time.strptime(str(self.startHour) + ":00", "%H:%M"))
        endHourStr = time.strftime("%H:%M", time.strptime(str(self.endHour) + ":00", "%H:%M"))
        returnStr = self.date.strftime("%Y-%m-%d") + " " + startHourStr + "~" + endHourStr + " "
        if self.isCancle:
            returnStr += "违约金 " + str(self.cost) + " 元"
        else:
            returnStr += str(self.cost) + " 元"
        return returnStr

    def __cmp__(self, s):
        if self.date < s.date:
            return -1
        elif self.date > s.date:
            return 1
        else:
            if self.startHour < s.startHour:
                return -1
            else:
                return 1

    def __eq__(self, bookMessage):
        attrNames = ["user", "date", "time", "area"]
        isEqual = True
        if self.isCancle:
            isEqual = False
        for item in attrNames:
            selfAttr = getattr(self, item, None)
            otherAttr = getattr(bookMessage, item, None)
            if not (selfAttr and otherAttr and selfAttr == otherAttr):
                isEqual = False
        return isEqual

    def _format_date(self, dateStr):
        try:
            return datetime.datetime.strptime(dateStr, "%Y-%m-%d")
        except Exception as e:
            self.isValid = False
            return None

    def _format_time(self, timeStr):
        continueFlag = self._get_starthour_endhour(timeStr)
        if continueFlag:
            return BookingTime((self.startHour, self.endHour))
        else:
            self.isValid = False
            return None

    def _get_starthour_endhour(self, durationStr):
        timeList = durationStr.split("~")
        if len(timeList) != 2:
            return False
        startHourNum = self._get_hour_num(timeList[FIRST])
        endHourNum = self._get_hour_num(timeList[SECOND])
        if startHourNum is ERROR or endHourNum is ERROR or startHourNum >= endHourNum:
            return False
        else:
            self.startHour = startHourNum
            self.endHour = endHourNum
            return True

    def _get_hour_num(self, timeStr):
        timeSplit = timeStr.split(":")
        if self._is_time_valid(timeSplit):
            return int(timeSplit[FIRST])
        else:
            return ERROR

    def _is_time_valid(self, timeSplit):
        return len(timeSplit) == 2 and timeSplit[SECOND] == "00" and BookingTime.is_open(timeSplit[0])

    def _format_cancle(self, cancelStr):
        if cancelStr is None:
            return False
        if cancelStr == "C":
            return True
        else:
            self.isValid = False
            return False
