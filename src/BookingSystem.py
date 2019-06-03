# coding=utf-8
'''
Created on 20190601

@author: --
'''
from src.BadmintonArea import BadmintonArea
from src.BookingMessage import BookingMessage
from src.Config import AREA_NAME_DEFINE, BOOKING_RESPONSE_DEFINE,\
    BOOKING_INVALID, BOOKING_MESSAGE_LENGHT, AREA, USER, DATE,\
    TIME, CANCLE_MESSAGE_LENGHT, CANCEL


class BookingSystem(object):
    '''
    预定系统，对外只提供预定和总计方法，维护场地实例
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.areas = self._ready_area()

    def _ready_area(self):
        areas = {}
        for name in AREA_NAME_DEFINE:
            areas.update({name: BadmintonArea(name)})
        return areas

    def start_booking(self, message):
        isValid, bookingMessageObjct = self._format_message(message)
        if isValid and bookingMessageObjct.isValid:
            areaObject = self.areas.get(bookingMessageObjct.area)
            if bookingMessageObjct.isCancle:
                return areaObject.cancel_booking(bookingMessageObjct)
            else:
                return areaObject.new_booking(bookingMessageObjct)
        else:
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID)

    def _format_message(self, message):
        paramsList = message.split(" ")
        if self._is_book_message(paramsList):
            return True, BookingMessage(paramsList[USER], paramsList[DATE], paramsList[TIME], paramsList[AREA])
        elif self._is_cancel_message(paramsList):
            return True, BookingMessage(paramsList[USER], paramsList[DATE], paramsList[TIME], paramsList[AREA], paramsList[CANCEL])
        else:
            return False, None

    def _is_book_message(self, paramsList):
        return len(paramsList) == BOOKING_MESSAGE_LENGHT and paramsList[AREA] in AREA_NAME_DEFINE

    def _is_cancel_message(self, paramsList):
        return len(paramsList) == CANCLE_MESSAGE_LENGHT and paramsList[AREA] in AREA_NAME_DEFINE

    def get_subtotal(self):
        subTotalMessage = ["收入汇总", "---"]
        subTotalMoney = 0
        for item in AREA_NAME_DEFINE:
            subTotalMessage.append("场地:" + item)
            areaObject = self.areas.get(item)
            subTotalMessage.extend(areaObject.get_booking_detail_list())
            subTotalMessage.append("小计：" + str(areaObject.get_subtotal()) + " 元")
            subTotalMoney += areaObject.get_subtotal()
            if (AREA_NAME_DEFINE.index(item) != (len(AREA_NAME_DEFINE) - 1)):
                subTotalMessage.append("")
            else:
                subTotalMessage.append("---")
        subTotalMessage.append("总计：" + str(subTotalMoney) + " 元")
        return subTotalMessage
