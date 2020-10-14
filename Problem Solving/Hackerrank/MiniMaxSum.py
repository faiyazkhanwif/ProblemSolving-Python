#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #insertion sort
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    minsum = 0
    maxsum = 0
    for m in range (0,len(arr)-1):
        minsum+=arr[m]
    arrtemp = arr
    arrtemp.reverse()
    for n in range (0,len(arrtemp)-1):
        maxsum+=arr[n]
    print(minsum, end=' ')
    print(maxsum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
