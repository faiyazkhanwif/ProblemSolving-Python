#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    count = 1
    for i in range (n+1):
        if i == 0:
            print(count)
        elif i!=0 and i%2 != 0:
            count*=2
            print(count)
        elif i!=0 and i%2 == 0:
            count+=1
            print(count)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
