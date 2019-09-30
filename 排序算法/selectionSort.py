#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @File: selectionSort.py
# @Time: 2019/09/30 21:30:21
# @Author: moli
# @Version: python3
# @Contact: guiczhang@163.com
# @blog: https://blog.csdn.net/u014421797

# DESCRIPTION:选择排序算法

def findMin(arr):
    """
    查找最小元素
    """
    smallest = arr[0]   # 存储最小值
    small_index = 0     # 存储索引

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            small_index = i
    return small_index      # 返回索引值

def selectionSort(arr):
    """
    选择排序算法
    """
    sort_arr = []      # 存储排序后的结果
    
    while arr:
        small_index = findMin(arr)
        sort_arr.append(arr.pop(small_index))   # 注意观察pop操作

    return sort_arr

S = [5, 10, 7, 3, 99]
T = selectionSort(S)
print(T)

