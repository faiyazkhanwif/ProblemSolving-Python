#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 1
    count =0
    countlist = []
    while i<len(c):
        if i==len(c)-1:
            if c[i] == 0:
                count+=1
                countlist.append(count)
                break
        else:
            if c[i]==1:
                count+=2
                countlist.append(count)
                i+=2
            elif c[i]==0 and c[i+1]==0:
                count+=2
                countlist.append(count)
                i+=2
            else:
                count+=1
                countlist.append(count)
                i+=1
    return len(countlist)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
