#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    hp=100
    if k>=len(c):
        i=k-len(c)
    else:
        i=k
    while i <= len(c):
        if i == 0:
            if c[i] == 1:
                hp -= 2
            hp -= 1
            break
        if c[i] == 1:
            hp -= 2
        hp -= 1
        print(hp)
        if (len(c) - 1) - i < k:
            i = i + k - len(c)
        else:
            i += k
    return hp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
