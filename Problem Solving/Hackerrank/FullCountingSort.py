#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr,arr1):
    temp = []
    res = []
    for i in range(0, max(arr1)+1):
        temp.append(i)
    for i in range(len(temp)):
        x = arr1.count(temp[i])
        temp[i] = x
    for i in range(len(temp)):
        res = res + [i] * temp[i]
    need = [[]]*len(arr1)
    for i in range(len(arr1)):
        if arr1[i]==arr[i][0]:
            need[arr1[i]]=need[arr1[i]]+[arr[i][1]]
    return need
if __name__ == '__main__':
    n = int(input().strip())

    arr = []
    arr1 = []
    for i in range(n):
        arr.append(input().rstrip().split())
        arr[i][0] = int(arr[i][0])
        arr1.append(arr[i][0])
        if i<n/2:
            arr[i][1]='-'
    #print(arr)
    #print(arr1)
    ans = countSort(arr,arr1)
    for i in range(len(ans)):
        print(*ans[i],end=' ')