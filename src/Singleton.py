# coding=utf-8
'''
Created on 20190601

@author: WLX
'''


def Singleton(cls):

    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

if __name__ == '__main__':
    pass
