#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    count = 0
    for i in range (0,n):
        count += 1
        countsp = 0
        for j in range (0,count):
            space = n - count
            if countsp == 0:
                for k in range (0,space):
                    print(' ',end='')
            print('#',end='')
            countsp+=1
        print()
if __name__ == '__main__':
    n = int(input())

    staircase(n)
