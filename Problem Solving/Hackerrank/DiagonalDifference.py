#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    matrix = arr
    ltor = 0
    rtol = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ltor = ltor + matrix[i][i]
            break
    for m in range(len(matrix)):
        temp = []
        for n in range(len(matrix[m]) - 1, -1, -1):
            temp.append(matrix[m][n])
        for o in range(len(temp)):
            rtol = rtol + temp[m]
            break
    result = abs(ltor - rtol)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
