# coding=utf-8
'''
Created on 20190601

@author: --
'''
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from src.BookingSystem import BookingSystem


bookSystem = BookingSystem()

if __name__ == '__main__':
    while True:
        inputMessage = raw_input("")
        if inputMessage == "":
            subTotalMessageList = bookSystem.get_subtotal()
            for item in subTotalMessageList:
                print "> " + item
        else:
            print "> " + bookSystem.start_booking(inputMessage)
