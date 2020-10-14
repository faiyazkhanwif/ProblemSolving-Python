#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n==0:
        return 1
    else:
        result = 1
        for i in range(n,0,-1):
            result = result*i
        return result

#recursive
def extraaLongFactorials(n):
    if n==0:
        return 1
    else:
        result = n*extraaLongFactorials(n-1)
        return result

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
    print(extraaLongFactorials(n))

