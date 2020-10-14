#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    #print(contests)
    totluck = 0
    impcon = 0
    impconarr=[]
    for i in range(len(contests)):
        totluck = totluck+contests[i][0]
        if contests[i][1]==1:
            impcon+=1
            impconarr.append(contests[i][0])
    impconarr.sort()
    #print(totluck)
    #print(impcon)
    #print(impconarr)
    for i in range(impcon-k):
        totluck=totluck-(impconarr[i]*2)
    return totluck

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print(result)