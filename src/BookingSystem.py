# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
from src.BadmintonArea import BadmintonArea
from src.BookMessage import BookMessage


AREA_NAME_DEFINE = ["A", "B", "C", "D"]
BOOKING_INVALID = USER = 0
BOOKING_SUCCESS = DATE = 1
BOOKING_CONFLICT = TIME = 2
CANCLE_NOT_EXIST = AREA = 3
BOOKING_MESSAGE_LENGHT = CANCLE = 4
CANCLE_MESSAGE_LENGHT = 5
BOOKING_RESPONSE_DEFINE = {BOOKING_INVALID: "Error: the booking is invalid!",
                           BOOKING_SUCCESS: "Success: the booking is accepted!",
                           BOOKING_CONFLICT: "Error: the booking conflicts with existing bookings!",
                           CANCLE_NOT_EXIST: "Error: the booking being cancelled does not exist!"}


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
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_SUCCESS)
        else:
            return BOOKING_RESPONSE_DEFINE.get(BOOKING_INVALID)

    def _format_message(self, message):
        paramsList = message.split(" ")
        if len(paramsList) == BOOKING_MESSAGE_LENGHT and paramsList[AREA] in AREA_NAME_DEFINE:
            return True, BookMessage(paramsList[USER], paramsList[DATE], paramsList[TIME], paramsList[AREA])
        elif len(paramsList) == CANCLE_MESSAGE_LENGHT and paramsList[AREA] in AREA_NAME_DEFINE:
            return True, BookMessage(paramsList[USER], paramsList[DATE], paramsList[TIME], paramsList[AREA], paramsList[CANCLE])
        else:
            return False, None
