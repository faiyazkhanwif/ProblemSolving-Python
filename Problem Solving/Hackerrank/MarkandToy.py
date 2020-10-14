#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    print(prices)
    budget = k
    count = 0
    for i in range(len(prices)):
        budget = budget-prices[i]
        if budget >= 0:
            count+=1
        else:
            break
    return count
if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)

