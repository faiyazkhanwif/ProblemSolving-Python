#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    denominator = len(arr)
    numerpos = 0
    numerneg = 0
    numerneut = 0
    for i in arr:
        if i>0:
            numerpos+=1
        elif i<0:
            numerneg+=1
        else:
            numerneut+=1
    print(numerpos/denominator)
    print(numerneg/denominator)
    print(numerneut/denominator)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
