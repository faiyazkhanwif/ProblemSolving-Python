#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER d
#
#Got 1.05, hard contest problem,998th place
def minimumMoves(s, d):
    test_str = s
    res = [test_str[x:y] for x, y in combinations(
        range(len(test_str) + 1), r=2)]
    resm = []
    #    print(res)
    for i in range(len(res)):
        if len(res[i]) >= d:
            resm.append(res[i])
    #    print(resm)

    count = []
    for i in range(len(resm)):
        if resm[i].find('1') == -1:
            count.append(0)
    # print(count)

    zcount = 0
    zplacel = []
    for i in range(len(test_str)):
        if test_str[i] == '0':
            zcount += 1
            zplacel.append(i)
    temp = []
    for i in range(len(test_str)):
        temp.append(test_str[i])
    if len(count) == 0:
        return (0)
    elif len(count) == 1:
        return (1)
    else:
        switch = 1
        for m in range(zcount):
            for i in range(len(test_str)):
                if temp[i] != '1':
                    temp[i] = '1'
                    sp = ''
                    ns = sp.join(temp)
                    resint = [ns[x:y] for x, y in combinations(
                        range(len(ns) + 1), r=2)]
                    resmint = []
                    for j in range(len(resint)):
                        if len(resint[j]) >= d:
                            resmint.append(resint[j])

                    countint = []
                    for j in range(len(resmint)):
                        temp = []
                        for k in range(len(resmint[j])):
                            temp.append(resmint[j][k])
                        onecount = 0
                        for k in range(len(temp)):
                            if temp[k] == '1':
                                onecount += 1
                        if onecount == 0:
                            countint.append(0)
                            onecount = 0
                    if len(countint) == 0:
                        return (i + 1)
                        switch = 0
                        break
                if switch == 0:
                    break
            if switch == 0:
                break
#answer
def minimumMoves(s, d):
    assert 1 <= d <= len(s) <= 1000000

    ct = 0
    ans = 0
    s += '1'
    for i in s:
        if i == '0':
            ct += 1
        else:
            ans += ct // d
            ct = 0
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()
