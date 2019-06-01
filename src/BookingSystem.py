# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
from src.BadmintonArea import BadmintonArea
from src.BookMessage import BookMessage
from src.Config import AREA_NAME_DEFINE, BOOKING_RESPONSE_DEFINE,\
    BOOKING_INVALID, BOOKING_MESSAGE_LENGHT, AREA, USER, DATE,\
    TIME, CANCLE_MESSAGE_LENGHT, CANCEL


class BookingSystem(object):
    '''
    classdocs
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
        isValid, bookMessageObjct = self._format_message(message)
        if isValid and bookMessageObjct.isValid:
            areaObject = self.areas.get(bookMessageObjct.bookArea)
            if bookMessageObjct.isCancle:
                return areaObject.cancelBook(bookMessageObjct)
            else:
                return areaObject.newBook(bookMessageObjct)
        else:
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID)

    def _format_message(self, message):
        paramsList = message.split(" ")
        if len(paramsList) == BOOKING_MESSAGE_LENGHT and paramsList[AREA] in AREA_NAME_DEFINE:
            return True, BookMessage(paramsList[USER], paramsList[DATE], paramsList[TIME], paramsList[AREA])
        elif len(paramsList) == CANCLE_MESSAGE_LENGHT and paramsList[AREA] in AREA_NAME_DEFINE:
            return True, BookMessage(paramsList[USER], paramsList[DATE], paramsList[TIME], paramsList[AREA], paramsList[CANCEL])
        else:
            return False, None

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
