# coding=utf-8
'''
Created on 20190601

@author: --
'''
# 存放预设
# 场地编号
AREA_NAME_DEFINE = ["A", "B", "C", "D"]

# 消息代码设定，消息字段位置
ERROR = -1
BOOKING_INVALID = USER = FIRST = 0
BOOKING_SUCCESS = DATE = SECOND = 1
BOOKING_CONFLICT = TIME = BINARY = 2
CANCEL_NOT_EXIST = AREA = 3
BOOKING_MESSAGE_LENGHT = CANCEL = 4
CANCLE_MESSAGE_LENGHT = Friday = 5

# 消息设定
BOOKING_RESPONSE_DEFINE = {BOOKING_INVALID: "Error: the booking is invalid!",
                           BOOKING_SUCCESS: "Success: the booking is accepted!",
                           BOOKING_CONFLICT: "Error: the booking conflicts with existing bookings!",
                           CANCEL_NOT_EXIST: "Error: the booking being cancelled does not exist!"}
# 各阶段单价
THIRTY_CNY = 30
FORTY_CNY = 40
FIFTY_CNY = 50
SIXTY_CNY = 60
EIGHTY_CNY = 80

WEEKDAY_CANCEL_DISCOUNT = 0.5
WEEKEND_CANCEL_DISCOUNT = 0.25

# 需求设定羽毛球场从早上9点到晚上10点，且最小单位是为小时
# 我们将这13个小时是否被预定以01形式表示，即对每次预定时间段由13位的byte来表示
NO_BOOKED = "0"
BOOKED = "1"
BADMINTON_OPEN_HOUR = 9
BADMINTON_URATION_HOURS = 13
