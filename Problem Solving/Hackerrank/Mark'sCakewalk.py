#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort()
    calorie.reverse()
    #print(calorie)
    n = 0
    minmile = 0
    for i in range(len(calorie)):
        minmile = minmile + (2 ** n) * calorie[i]
        n += 1
    return minmile


if __name__ == '__main__':
    n = int(input())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    print(result)
