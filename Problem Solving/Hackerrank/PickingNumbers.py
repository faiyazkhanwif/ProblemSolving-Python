#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

#15 points out of 20. 2 test cases did not match.

#MEDIUM DIFFICULTY
def pickingNumbers(a):
    rows, cols = (len(a), 1)
    mylist = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(0,len(a)):
        mylist[i].append(a[i])
        for j in range(1,len(a)):
            if abs(a[i]-a[j])<=1:
                mylist[i].append(a[j])
    print(mylist)
    return (len(max(mylist))-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()


#perfect code from discussion
from collections import Counter
def pickingNumbers(a):
    a = Counter(a)
    maxi = 0
    for k in sorted(a):
        m = a[k]+a.get(k+1,0)
        if maxi<m:
            maxi=m
    return maxi
input()
a = map(int,input().split())
print(pickingNumbers(a))