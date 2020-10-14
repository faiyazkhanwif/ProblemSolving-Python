#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
#MEDIUM DIFFICULTY
def formingMagicSquare(s):
    sample = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8], ]
    mylist = []
    finallist = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            mylist.append(s[i][j])
    print(mylist)
    for i in range(len(sample)):
        compresult = 0
        for j in range(len(sample[i])):
            result = abs(sample[i][j]-mylist[j])
            compresult+=result
        finallist.append(compresult)
    print(finallist)
    return min(finallist)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
