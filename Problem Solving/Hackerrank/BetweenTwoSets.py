#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#DID NOT SOLVE ALL THE TEST CASES

def getTotalX(a, b):
    maxela = max(a)
    tempkey = maxela
    temp = []
    while tempkey <= min(b):
        if tempkey%maxela==0:
            temp.append(tempkey)
        tempkey+=1
    for j in range(len(a)):
        for k in range(len(temp)):
            if temp[k]%a[j] == 0:
                continue
            else:
                temp.remove(temp[k])
    for m in range(len(temp)):
        for n in range (len(b)):
            if b[n]%temp[m] == 0:
                continue
            else:
                temp.remove(temp[m])
    return len(temp)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #first_multiple_input = input().rstrip().split()

    #n = int(first_multiple_input[0])

    #m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    #fptr.write(str(total) + '\n')

    #fptr.close()
