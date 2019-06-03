# coding=utf-8
'''
Created on 20190601

@author: --
'''
from src.BookingTime import BookingTime
from src.Config import THIRTY_CNY, FIFTY_CNY, EIGHTY_CNY, SIXTY_CNY, FORTY_CNY,\
    WEEKEND_CANCEL_DISCOUNT, WEEKDAY_CANCEL_DISCOUNT, Friday, BINARY,\
    BADMINTON_URATION_HOURS, FIRST, SECOND


class BookingCost(object):
    '''
       各小时的单价定义，提供预定时间的总价，以及取消时的违约金
    '''
    HOUR_9_TO_12 = BookingTime((9, 12))
    HOUR_12_TO_18 = BookingTime((12, 18))
    HOUR_18_TO_20 = BookingTime((18, 20))
    HOUR_20_TO_22 = BookingTime((20, 22))
    HOUR_18_TO_22 = BookingTime((18, 22))
    WEEKDAY_PRICE = [[HOUR_9_TO_12, HOUR_12_TO_18, HOUR_18_TO_20, HOUR_20_TO_22],
                     [THIRTY_CNY, FIFTY_CNY, EIGHTY_CNY, SIXTY_CNY]]
    WEEKEND_PRICE = [[HOUR_9_TO_12, HOUR_12_TO_18, HOUR_18_TO_22],
                     [FORTY_CNY, FIFTY_CNY, SIXTY_CNY]]

    def __init__(self, date, bookingTime, isCancel=False):
        '''
        @date 预定日志，datetime对象
        @bookingTime BookingTime实例
        @isCancel boolean
        '''
        self.isWeekend = self._is_weekend(date)
        self.bookingCost = 0
        self.income = 0
        self.cost = 0
        self._calc_booking_cost(bookingTime)
        self._calc_cost_and_income(isCancel)

    def _calc_booking_cost(self, bookingTime):
        window = BookingTime.new_booking_time() + 1
        for _ in range(BADMINTON_URATION_HOURS):
            if bookingTime.contain(window):
                self.bookingCost += self._get_price_peer_hour(window)
            window <<= 1

    def _calc_cost_and_income(self, isCancel):
        if isCancel:
            if self.isWeekend:
                self.cost = int(self.bookingCost * WEEKEND_CANCEL_DISCOUNT)
            else:
                self.cost = int(self.bookingCost * WEEKDAY_CANCEL_DISCOUNT)
            self.income = self.cost - self.bookingCost
        else:

            self.cost = self.income = self.bookingCost

    def _get_price_peer_hour(self, whichHour):
        if self.isWeekend:
            hourDurtion = self.WEEKEND_PRICE[FIRST]
            priceDefine = self.WEEKEND_PRICE[SECOND]
        else:
            hourDurtion = self.WEEKDAY_PRICE[FIRST]
            priceDefine = self.WEEKDAY_PRICE[SECOND]
        for i in range(len(hourDurtion)):
            if hourDurtion[i].contain(whichHour):
                return priceDefine[i]
        return 0

    def _is_weekend(self, date):
        return date.isoweekday() > Friday
