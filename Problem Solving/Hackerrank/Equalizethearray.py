#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(s):
    s.sort()
    print(s)
    countlist = []
    for i in range(len(s)):
        countlist.append(s.count(s[i]))
    temp = max(countlist)
    ans = len(s) - temp
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
