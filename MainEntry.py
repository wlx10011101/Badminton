# coding=utf-8
'''
Created on 20190601

@author: linkswei
'''
import sys
from src.BookingSystem import BookingSystem

bookSystem = BookingSystem()

if __name__ == '__main__':
    while True:
        inputMessage = raw_input("")
        if inputMessage == "":
            subTotalMessageList = bookSystem.get_subtotal()
            for item in subTotalMessageList:
                print "> " + item + "\r\n"
        else:
            print "> " + bookSystem.start_booking(inputMessage)
