#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    checklist=[]
    for i in range(len(ar)):
        if ar[i] in checklist:
            continue
        else:
            elcount = ar.count(ar[i])
            if elcount/2>0:
                temp = int(elcount/2)
                pairs+=temp
            checklist.append(ar[i])
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
