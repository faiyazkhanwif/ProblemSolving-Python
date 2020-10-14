#!/bin/python3

import math
import os
import random
import re
import sys

#MEDIUM DIFFICULTY
#7 out of 14
def formingMagicSquare(s):
    countres=0
    row = []
    col=[]
    #print(s)
    diagsum=0
    colcount = 0
    colsum = 0
    coltemp=[]
    colsumtmp=[]
    colarr=[]
    altdiagsum=0
    for i in range(len(s)):
        diagsum += s[i][i]
    #print(diagsum)
    for i in range(len(s)):
        r= sum(s[i])
        #print(r)
        if r!=diagsum:
            countres+=1
            row.append(i+1)
    #print(row)
    n=0
    k = len(s)*len(s[0])
    #print(k)
    for i in range(k):
        colsum += s[n][colcount]
        coltemp.append(s[n][colcount])
        n+=1
        if n==len(s[0]):
            colsumtmp.append(colsum)
            colarr.append(coltemp)
            #print(colarr)
            colsum=0
            coltemp=[]
            colcount+=1
            #print(n)
            n=0
    #print(colarr)
    #print(colsumtmp)
    for i in range(len(colsumtmp)):
        if colsumtmp[i]!=diagsum:
            col.append(-1*(i+1))
            countres+=1
    col.sort()
    #print(col)
    kalt = len(s[0])-1
    for i in range(0,len(s)):
        #print(s[i])
        altdiagsum+=s[i][kalt]
        #print(s[i][kalt])
        kalt-=1
    #print(altdiagsum)
    if altdiagsum!=diagsum:
        countres+=1
    print(countres)
    for i in range(len(row)):
        print(i)
    for i in range(len(col)):
        print(col[i])
    if altdiagsum!=diagsum:
        print(0)
if __name__ == '__main__':
    n = int(input())
    s = []
    for _ in range(n):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
