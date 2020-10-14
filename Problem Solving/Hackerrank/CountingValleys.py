#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
# gets 3 points as there is some issues with understanding the question.
def countingValleys(n, s):
    count=0
    i = 0
    while i <= n - 2:
        if i!=n-2:
            if s[i]=='D' and s[i+1]=='D' and s[i+1+1]=='U':
                count+=1
                i+=1
            else:
                i+=1
        else:
            break
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#Working code from forum that gets 10 points
def countingValleys(n, s):
    valley=0
    land = 0
    for i in s:
        if i=='U':
            land+=1
        if i=='D':
            land+=-1
        if land==0 and i=='U':
           valley+=1
    return valley