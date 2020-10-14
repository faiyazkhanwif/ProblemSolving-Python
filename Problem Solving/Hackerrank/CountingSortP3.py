#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    temp = []
    res = []
    for i in range(0,max(arr)+1):
        temp.append(i)
    for i in range(len(temp)):
        x = arr.count(temp[i])
        temp[i]=x
    #print(temp)
    for i in range(0,100):
        if i < len(temp) and i==0:
            res.append((temp[i]))
        elif i<len(temp) and i>0:
            res.append(temp[i]+res[i-1])
        else:
            res.append(res[i-1])
    return res
if __name__ == '__main__':
    arr=[]
    arr1=[]
    n = int(input())
    for i in range(n):
        arr =arr+ [list(input().rstrip().split())]
        arr[i][0]=int(arr[i][0])
        arr1.append(arr[i][0])
    #print(arr)
    #print(arr1)
    result = countingSort(arr1)
    print(*result)


#Optimized code for longer inputs
n = int(input())
ar = []
for i in range(n):
    ar.append(input().split())
a = [0 for i in range(100)]
for i in ar:
    a[int(i[0])] += 1
count = 0
for i in range(len(a)):
    count += a[i]
    a[i] = count
print(*a)