#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
#Medium
def appendAndDelete(s, t, k):
    initialstring = s
    desiredstring = t
    steps = k
    countlist = []
    i = 0
    j = 0
    count = 0
    while i < (len(initialstring)):
        while j < (len(desiredstring)):
            if initialstring[i] == desiredstring[j]:
                j += 1
                count += 1
                break
            else:
                j += 1
                count = 0
        i += 1
        countlist.append(count)
    match = max(countlist)
    initemp = abs(len(initialstring) - match)
    destemp = abs(len(desiredstring) - match)
    if initialstring==desiredstring:
        return 'Yes'
    elif len(initialstring) + len(desiredstring) <= steps:
        return 'Yes'
    elif initemp + destemp <= steps:
        if initemp+destemp<steps:
            if len(initialstring)+destemp<=steps:
                return 'No'
            elif match+initemp+destemp>steps and len(initialstring)==len(desiredstring):
                return 'No'
            else:
                print("ami ekhane")
                return 'Yes'
        else:
            print("ami ekhane")
            return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
