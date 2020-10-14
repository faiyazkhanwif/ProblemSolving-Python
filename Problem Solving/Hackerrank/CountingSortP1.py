#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    temp = []
    for i in range(0,max(arr)+1):
        temp.append(i)
    for i in range(len(temp)):
        x = arr.count(temp[i])
        temp[i]=x
    return temp
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(*result)
