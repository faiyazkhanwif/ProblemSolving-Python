#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the closestNumbers function below.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    i = -1
    j = 0
    while j < len(arr):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
            global z
        elif arr[j] > pivot:
            j += 1
        else:
            j += 1
    arr.insert(i + 1, pivot)
    arr.pop(len(arr) - 1)
    arr = quicksort(arr[0:i + 1]) + [pivot] + quicksort(arr[i + 2:len(arr)])
    # print(arr)
    return arr


def closestNumbers(arr):
    lst = quicksort(arr)
    #print(lst)
    tempval = []
    ans = []
    for val in combinations(arr,2):
        tmp = val[0]-val[1]
        tempval.append(abs(tmp))
    minimum = min(tempval)
    #print(minimum)
    for i in range(len(lst)):
        val = lst[i] + minimum
        if val in lst:
            ans.append((lst[i], val))
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    for i in range(len(result)):
        print(*result[i],end=' ')
