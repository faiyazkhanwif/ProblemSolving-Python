#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the acmTeam function below.

#Code working, but fails some test cases because of timeout
def acmTeam(topic):
    data = combinations(topic, 2)
    subsets = list(set(data))
    countlist=[]
    for i in range(len(subsets)):
        count=0
        temp = list(subsets[i])
        for k in range(len(temp[0])):
            if int(temp[0][k])|int(temp[1][k])==1:
                count+=1
        countlist.append(count)
    maximum = max(countlist)
    print(maximum)
    waycount=0
    for i in range(len(countlist)):
        if countlist[i]==maximum:
            waycount+=1
    print(waycount)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

#Solution from discussion
def acmTeam(topic):
    count = 0
    max_ = 0
    for c in combinations(topic, 2):
        sum_ = bin(int(c[0], 2)|int(c[1], 2)).count('1')
        if sum_ > max_:
            count = 1
            max_ = sum_
        elif sum_ == max_:
            count += 1
    return (max_, count)