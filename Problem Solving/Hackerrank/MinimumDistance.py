#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    res = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j and a[i]==a[j]:
                res.append(abs(i-j))
    if len(res)==0:
        return -1
    else:
        return min(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
