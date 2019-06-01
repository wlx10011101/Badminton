# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
from src.Config import BOOKING_RESPONSE_DEFINE, BOOKING_CONFLICT,\
    BOOKING_SUCCESS, CANCEL_NOT_EXIST


class BadmintonArea(object):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.hasBookeByDatetime = {}
        self.bookHistoryList = []
        self.totalIncome = 0

    def newBook(self, bookMessage):
        if bookMessage.bookDate in self.hasBookeByDatetime:
            bookedTime = self.hasBookeByDatetime.get(bookMessage.bookDate)
            if bookedTime & bookMessage.bookTime:
                return BOOKING_RESPONSE_DEFINE.get(BOOKING_CONFLICT)
            else:
                return self._susccess_book(bookMessage, bookedTime)
        else:
            return self._susccess_book(bookMessage)

    def _susccess_book(self, bookMessage, lastBookTime=None):
        if lastBookTime:
            self.hasBookeByDatetime.update({bookMessage.bookDate: lastBookTime | bookMessage.bookTime})
        else:
            self.hasBookeByDatetime.update({bookMessage.bookDate: bookMessage.bookTime})
        self._fresh_history(bookMessage)
        self.totalIncome += bookMessage.cost
        return BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)

    def cancelBook(self, bookMessage):
        if bookMessage in self.bookHistoryList:
            bookTime = self.hasBookeByDatetime.get(bookMessage.bookDate)
            self.hasBookeByDatetime.update({bookMessage.bookDate: bookTime & (~ bookMessage.bookTime)})
            self._fresh_history(bookMessage, True)
            self.totalIncome += (bookMessage.cost - bookMessage.noCancelCost)
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        else:
            return BOOKING_RESPONSE_DEFINE.get(CANCEL_NOT_EXIST)

    def _fresh_history(self, bookMessage, isCancel=False):
        if isCancel:
            for item in self.bookHistoryList:
                if bookMessage == item and item.isCancle is False:
                    self.bookHistoryList.remove(item)
        self.bookHistoryList.append(bookMessage)
        self.bookHistoryList = sorted(self.bookHistoryList)

    def get_subtotal(self):
        return self.totalIncome

    def get_booking_detail_list(self):
        return [str(i) for i in self.bookHistoryList]
