#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    z=0
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i + 1] = arr[i]
            arr[i]=temp
            k=i
            z+=1
            for j in range(i-1,-1,-1):
                if arr[j]>arr[k]:
                    temp1 = arr[j]
                    arr[j] = arr[k]
                    arr[k] = temp1
                    k=k-1
                    z+=1
    print(*arr)
    print('Running Time:',z)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
