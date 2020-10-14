#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
#Got 8 points out of 20 for runtime error
def circularArrayRotation(a, k, queries):
    for i in range(k):
        sres = []
        sres.append(a[len(a) - 1])
        for j in range(len(a) - 1):
            sres.append(a[j])
        a.clear()
        a = sres.copy()
    for i in range(len(queries)):
        print(a[queries[i]])
if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

#Perfect solution for all testcases
from collections import deque
# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    dq = deque(a, len(a))
    dq.rotate(k)

    return [dq[num] for num in queries]