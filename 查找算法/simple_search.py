#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   simple_search.py
@Time    :   2019/09/11 09:37:00
@Author  :   moli 
@Version :   python3
@Contact :   guiczhang@163.com
@blog :   https://blog.csdn.net/u014421797
'''

def simple_search(mylist, item):
    """
    简单查找
    list:不需要列表有序，因为是遍历所有的值进行查找
    item:查找目标
    """
    for i in range(len(mylist)):
        if mylist[i] == item:
            index = i
            count = i + 1
            return index, count
    return None, len(mylist)

import time

mylist = [i for i in range(1, 100000)]
item = 99999
start = time.clock()
result, count = simple_search(mylist,item)
end = time.clock()
print('查找次数:', count)
print('目标所在下标为：',result)
print('目标值为：', mylist[result])
print('所用时间：',end-start)