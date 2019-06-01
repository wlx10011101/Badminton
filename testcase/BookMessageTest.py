# coding=utf-8
'''
Created on 2019年6月1日

@author: linkswei
'''
import sys
import unittest

from src.BookMessage import BookMessage


class BookMessageTest(unittest.TestCase):

    def testMessageValid(self):
        sys.argv = ['U01101', "2016-06-02 22:00~22:00", "A"]
        bookMessage = BookMessage(sys.argv)
        assert bookMessage.is_valid()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
