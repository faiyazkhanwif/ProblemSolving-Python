#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    firststart = 0
    laststart = 0
    i=1
    j=n
    while i<=n:
        if i == p or i-1==p:
            break
        else:
            firststart += 1
            i += 2
    while j>=0:
        if n%2!=0:
            if j == p or j-1==p:
                break
            else:
                j -= 2
                laststart += 1
        if n%2==0:
            if j == p or j + 1 == p:
                break
            else:
                j -= 2
                laststart += 1
    return min(firststart,laststart)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
