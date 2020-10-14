#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    i=1
    num = 3
    count = 3
    while i<=t:
        if i == 1:
            count = 3
            i+=1
        else:
            if count == 1:
                count = num*2
                num = count
                i+=1
            else:
                count-=1
                i+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()


#Simple solution using math formula
def strangeCounter(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
    print(rem-t+1)