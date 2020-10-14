#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    countlist = [len(arr)]
    while len(arr) > 1:
        temp = min(arr)
        while any(v == temp for v in arr):
            arr.remove(temp)
            print(arr)
        if not arr:
            break
        else:
            temp = min(arr)
            countlist.append(len(arr))
    return countlist

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)
    print(result)
