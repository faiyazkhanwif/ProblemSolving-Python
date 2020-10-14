#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases):
    for i in range (len(cases)):
        ans = []
        j = cases[i][0]
        length = cases[i][1]
        while j <= length:
            ans.append(n[j])
            j+=1
        print(min(ans))

if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

