#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    base=[]
    base2=[]
    ylist=[]
    for i in range (len(p)):
        base.append(i+1)
    for i in range (len(base)):
        for j in range (len(p)):
            if base[i]==p[j]:
                base2.append(j+1)
    for i in range(len(base2)):
        for j in range(0,len(p)):
            if base2[i]==p[j]:
                ylist.append(j+1)
    for i in range(0,len(ylist)):
        print(ylist[i])
if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
