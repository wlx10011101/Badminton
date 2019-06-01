# coding=utf-8
'''
Created on 2019��6��1��

@author: linkswei
'''
import unittest

from src.BookTime import BookTime


class BookTimeTest(unittest.TestCase):

    def test9To22(self):
        result = BookTime.coverTimeToByte(9, 22)
        print result, int("1111111111111", 2)
        assert result == int("1111111111111", 2)

    def test10To10(self):
        result = BookTime.coverTimeToByte(10, 10)
        print result, int("0000000000000", 2)
        assert result == int("0000000000000", 2)

    def test9To10(self):
        result = BookTime.coverTimeToByte(9, 10)
        print result, int("1000000000000", 2)
        assert result == int("1000000000000", 2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
