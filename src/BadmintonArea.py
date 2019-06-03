# coding=utf-8
'''
Created on 20190601

@author: --
'''
from src.BookingTime import BookingTime
from src.Config import BOOKING_RESPONSE_DEFINE, BOOKING_CONFLICT,\
    BOOKING_SUCCESS, CANCEL_NOT_EXIST


class BadmintonArea(object):
    '''
    场地类，处理单个场地的预定，记录预定消息
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.hasBookedByDatetime = {}
        self.bookingHistoryList = []
        self.totalIncome = 0

    def new_booking(self, bookMessage):
        areaBookedTime = self.hasBookedByDatetime.get(bookMessage.date, BookingTime())
        if areaBookedTime.is_conflict(bookMessage.time):
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_CONFLICT)
        else:
            self._fresh_booked_time(areaBookedTime, bookMessage)
            self._fresh_history(bookMessage)
            self.totalIncome += bookMessage.income
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)

    def cancel_booking(self, bookMessage):
        areaBookedTime = self.hasBookedByDatetime.get(bookMessage.date, BookingTime())
        if areaBookedTime.has_booking():
            self._fresh_booked_time(areaBookedTime, bookMessage, True)
            self._fresh_history(bookMessage, True)
            self.totalIncome += bookMessage.income
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        else:
            return BOOKING_RESPONSE_DEFINE.get(CANCEL_NOT_EXIST)

    def _fresh_booked_time(self, areaBookedTime, bookMessage, isCancel=False):
        if isCancel:
            newBookedTime = areaBookedTime.cut(bookMessage.time)
        else:
            newBookedTime = areaBookedTime.add(bookMessage.time)
        self.hasBookedByDatetime.update({bookMessage.date: newBookedTime})

    def _fresh_history(self, bookMessage, isCancel=False):
        if isCancel:
            self._remove_item_from_history(bookMessage)
        self.bookingHistoryList.append(bookMessage)
        self.bookingHistoryList = sorted(self.bookingHistoryList)

    def _remove_item_from_history(self, bookMessage):
        for item in self.bookingHistoryList:
            if item == bookMessage and item.isCancle is False:
                self.bookingHistoryList.remove(item)

    def get_subtotal(self):
        return self.totalIncome

    def get_booking_detail_list(self):
        return [str(i) for i in self.bookingHistoryList]
