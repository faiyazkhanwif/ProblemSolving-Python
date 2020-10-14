#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    res = []
    mini = 2147483647
    for var in combinations(arr, 2):
        res.append([var[0], var[1]])
    for i in range(len(res)):
        tmp = (abs(res[i][0]-res[i][1]))
        if tmp<mini:
            mini = tmp
    return mini

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)


#Efficient one liner
n,a = input(),sorted(map(int, input().split()))
print(min(abs(x-y) for x,y in zip(a,a[1:])))