#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    res = []
    temp = []
    ans = []
    maxperi = 0
    for var in combinations(sticks, 3):
        res.append([var[0], var[1], var[2]])
    #print(res)
    for i in range(len(res)):
        res[i].sort()
        tot = res[i][0]+res[i][1]+res[i][2]
        if tot-max(res[i])!=max(res[i]) and res[i][2]<res[i][1]+res[i][0]:
            temp.append(res[i])
    #print(temp)
    if len(temp)!=0:
        for i in range(len(temp)):
            tot = temp[i][0]+temp[i][1]+temp[i][2]
            if tot>maxperi:
                ans.append(temp[i])
                maxperi=tot
        #print(temp)
        return ans[len(ans)-1]
    else:
        return [-1]
if __name__ == '__main__':
    n = int(input())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    print(*result)