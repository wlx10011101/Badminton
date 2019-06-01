# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
from src.BookTime import BookTime, BADMINTON_URATION_HOURS
Friday = 5
THIRTY_CNY = 30
FORTY_CNY = 40
FIFTY_CNY = 50
SIXTY_CNY = 60
EIGHTY_CNY = 80

WEEKDAY_CANCLE_DISCOUNT = 0.5
WEEKEND_CANCLE_DISCOUNT = 0.25


class PriceHandler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.hour9To12 = BookTime.convertTimeToByte(9, 12)
        self.hour12To18 = BookTime.convertTimeToByte(12, 18)
        self.hour18To22 = BookTime.convertTimeToByte(18, 22)

        self.hour18To20 = BookTime.convertTimeToByte(18, 20)
        self.hour20To22 = BookTime.convertTimeToByte(20, 22)

    def peerHourInWeekday(self, whichHour):
        if whichHour & self.hour9To12:
            return THIRTY_CNY
        elif whichHour & self.hour12To18:
            return FIFTY_CNY
        elif whichHour & self.hour18To20:
            return EIGHTY_CNY
        elif whichHour & self.hour20To22:
            return SIXTY_CNY

    def peerHourInWeekend(self, whichHour):
        if whichHour & self.hour9To12:
            return FORTY_CNY
        elif whichHour & self.hour12To18:
            return FIFTY_CNY
        elif whichHour & self.hour18To22:
            return SIXTY_CNY

    def totalCost(self, date, hour, isCancle=False):
        totalCost = 0
        peerHourCalc = None
        isWeekend = self._is_weekend(date)
        if isWeekend:
            peerHourCalc = getattr(self, "peerHourInWeekend")
        else:
            peerHourCalc = getattr(self, "peerHourInWeekday")
        # 初始mask 0000000000001， 左移逐位与
        window = int("".join(["0" for _ in range(BADMINTON_URATION_HOURS - 1)]) + "1", 2)
        for _ in range(BADMINTON_URATION_HOURS):
            if hour & window:
                totalCost += peerHourCalc(window)
            window <<= 1
        if isCancle:
            if isWeekend:
                return totalCost * WEEKEND_CANCLE_DISCOUNT
            else:
                return totalCost * WEEKDAY_CANCLE_DISCOUNT
        else:
            return totalCost

    def _is_weekend(self, date):
        return date.isoweekday() > Friday
