#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    r = 5
    l=0
    lday = 0
    for i in range (1,n+1):
        if i ==1:
            l += math.floor(r/2)
            lday = l
        else:
            recip = lday*3
            lday =math.floor(recip/2)
            l+=lday
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
