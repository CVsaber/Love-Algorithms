#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   binary_search.py
@Time    :   2019/09/11 09:36:31
@Author  :   moli 
@Version :   python3
@Contact :   guiczhang@163.com
@blog :   https://blog.csdn.net/u014421797
'''

def binary_search(mylist, item):
    """
    二分查找
    list:有序列表,默认从小到大
    item:查找目标
    """
    low = 0     # 跟踪查找的列表部分
    high = len(mylist)-1
    count = 0   # 查找次数
    while low <= high:
        count += 1
        mid = (low + high)//2
        guess = mylist[mid]
        if guess == item:
            return mid, count
        if guess > item:
            high = mid - 1  # 猜大，舍弃后半部分
        else:
            low = mid + 1   # 猜小，舍弃前边部分
    return None, count

import time

mylist = [i for i in range(1, 100000)]
item = 99999
start = time.clock()
result, count = binary_search(mylist,item)
end = time.clock()
print('查找次数:', count)
print('目标所在下标为：',result)
print('目标值为：', mylist[result])
print('所用时间：',end-start)
