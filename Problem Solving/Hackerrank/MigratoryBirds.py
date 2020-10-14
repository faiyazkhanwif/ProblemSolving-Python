#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
#The solution below does not work for massive test inputs because of not being able to execute within the time limits
def migratoryBirds(arr):
    maxoccur = 0
    maxlist = []
    arr.sort()
    for i in range(len(arr)):
        maxoccur = arr.count(arr[i])
        maxlist.append(maxoccur)
        maxoccur = 0
    print(maxlist)
    rindex = maxlist.index(max(maxlist))
    return arr[rindex]

#Optimized solution that solves all test cases
def migratoryBirds(arr):
    count = [0]*6
    for t in arr:
        count[t] += 1
    return(count.index(max(count)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
