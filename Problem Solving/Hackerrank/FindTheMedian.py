#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
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
        elif arr[j] > pivot:
            j += 1
        else:
            j += 1
    arr.insert(i + 1, pivot)
    arr.pop(len(arr) - 1)
    arr = quicksort(arr[0:i + 1]) + [pivot] + quicksort(arr[i + 2:len(arr)])
    #print(arr)
    return arr

def findMedian(arr):
    temp = quicksort(arr)
    ans = temp[math.floor(len(temp)/2)]
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
