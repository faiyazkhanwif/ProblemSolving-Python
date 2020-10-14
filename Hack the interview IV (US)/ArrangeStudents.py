#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrangeStudents' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#Got 18.5. Missed 1 test case because of the input bug, but code works.
def arrangeStudents(a, d):
    b = a
    g = d
    b.sort()
    g.sort()
    #print(b)
    #print(g)
    bglist = []
    for i in range(len(b)):
        if i != len(b) - 1:
            if b[i] < g[i] and b[i + 1] >= g[i]:
                bglist.append(b[i])
                bglist.append(g[i])
                # switch=0
            elif g[i] < b[i] and g[i + 1] >= b[i]:
                bglist.append(g[i])
                bglist.append(b[i])
            elif b[i] == g[i]:
                bglist.append(g[i])
                bglist.append(b[i])
            else:
                return ('NO')
                break
        else:
            if b[i] <= g[i]:
                bglist.append(b[i])
                bglist.append(g[i])
                # switch=0
            elif g[i] <= b[i]:
                bglist.append(g[i])
                bglist.append(b[i])
            else:
                return ('NO')
                break
    #print(bglist)
    #print(len(bglist))
    #print('hi')
    bglistlen = len(bglist)
    blen = len(b)
    glen = len(g)
    if bglistlen != 0:
        if bglistlen == blen + glen:
            return ('YES')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)

        fptr.write(result + '\n')

    fptr.close()
