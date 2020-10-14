#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
n = int(input())
w = list(map(int, input().rstrip().split()))
cnt = n
count = 0
temp = []
#Fails 5 test cases because of recursion limit exceeding error
def toys(w):
    temp2=[]
    w.sort()
    tmp = min(w)
    length = len(w)
    #print(w)
    for i in range(0,length):
        if w[i]<=tmp+4:
            temp.append(w[i])
            global cnt
            cnt-=1
            #print(temp)
        else:
            temp2.append(w[i])
    global count
    count+=1
    w = temp2
    #print(w)
    #print(count)
    #print(cnt)
    if cnt!=0:
        toys(w)
    else:
        print(count)

result = toys(w)

#Perfect solution from discussion
N = int(input())
W = set(map(int, input().split()))

i = 0
while len(W) > 0:
    i += 1
    m = min(W)
    W = W.difference(set(range(m, m + 5)))

print(i)