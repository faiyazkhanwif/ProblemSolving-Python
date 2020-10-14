#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    base =arr
    arr2=[]
    count = 0
    i=0
    while i<k:
        if max(arr)==arr[count]:
            arr2.append(max(arr))
            arr[count]=-1
            count+=1
            #print(arr2)
            if len(arr2)==len(base):
                break
        else:
            temp = max(arr)
            tempind = arr.index(max(arr))
            temp2 = arr[count]
            #arr[count]=temp
            arr2.append(temp)
            arr[tempind] = temp2
            arr[count]=-1
            #print(arr2)
            if len(arr2)==len(base):
                break
            count+=1
            i+=1
    if len(arr2)!=len(base):
        for i in range(k,len(base)):
            arr2.append(base[i])
    return arr2
if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)
    print(*result)



#   Efficient perfect solution
def largestPermutation(k, arr, n):
    d = {}
    i = 0
    while i<n:
        d[arr[i]] = i
        i+=1
    i=0
    print(d)
    while n>0 and k>0:
        if arr[i]<n:
            tmp = d[n]
            arr[d[n]] = arr[i]
            arr[i] = n
            tmp = d[arr[d[n]]]
            d[arr[d[n]]] = d[n]
            d[n] = tmp
            k-=1
        n-=1
        i+=1
    return arr