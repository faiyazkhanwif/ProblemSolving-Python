#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days=0
    for m in range (i,j+1):
        reversedday = str(m)[::-1]
        dayresult = (m-int(reversedday))%k
        if dayresult==0:
            days+=1
        elif dayresult!=0:
            continue
    return days
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
