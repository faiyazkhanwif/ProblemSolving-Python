#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
#Fails 4 test cases because of not executing on time
def bigSorting(unsorted):
    ans = []
    for i in range(len(unsorted)):
        ans.append(int(unsorted[i]))
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

#Perfect efficient solution
def bigSorting(unsorted):
    unsorted.sort()
    unsorted.sort(key=len)
    return unsorted