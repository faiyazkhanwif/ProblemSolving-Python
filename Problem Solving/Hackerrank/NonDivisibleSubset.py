#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import chain, combinations

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#Medium/Hard problem
#Code works. However it's not efficient for high volume input. Gets runtime error
def nonDivisibleSubset(kd, s):
    test_str = s
    k=kd
    def powerset(a_set):
        s = list(a_set)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    res = list(powerset(test_str))
    #print(res)
    temp = []
    for i in range(len(res)):
        if len(res[i]) >= 2:
            temp.append(res[i])
    #print(temp)
    finalres = []
    for i in range(len(temp)):
        if len(temp[i]) == 2:
            if sum(temp[i]) % k != 0:
                finalres.append(temp[i])
                #print(str(i) + '= ' + str(temp[i]))
        if len(temp[i]) > 2:
            count=0
            data = combinations(temp[i],2)
            subsets = list(data)
            for j in range(len(subsets)):
                if sum(list(subsets[j]))%k==0:
                    count=1
            if count == 0:
                finalres.append(temp[i])
    lenglist = []
    for i in range(len(list(finalres))):
        lenglist.append(len(list(finalres[i])))
        if len(list(finalres[i]))==14:
            print(list(finalres[i]))
    print(lenglist)
    return max(lenglist)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()


#Perfect efficient solution from the discussion
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 04:20:47 2017

@author: amit.yadav
"""

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
count = 0
nums = list(map(int, input().strip().split(' ')))
remainder_list = []
for i in range(len(nums)):
    remainder_list.append(nums[i] % k)  # taking all the remainders

if 0 in remainder_list:  # if there is any number evenly divisible, just add one to count because, adding it with any other number wont divide by k
    count += 1
remainder_list = [x for x in remainder_list if
                  x != 0]  # and then remove all the 0 remainders (because there sum will always be divisible by k)
counter = [0] * k  # make a counter
for i in range(len(remainder_list)):
    counter[remainder_list[i]] += 1  # add one for each occurance of same remainder using it as index

index = []

for i in range(len(counter)):
    maxCount = max(counter)  # check the max value of  occurance of a remainder in the list
    maxIndex = counter.index(
        maxCount)  # and its index too (that is remainder actually since we used the empty list and got all values with remainder as index)
    if k - maxIndex not in index and maxCount != 0:  # the logic is, if the sum of two remainders are equal to k, then it will be divisble by k, so only add the max number of either
        index.append(maxIndex)
        if maxIndex * 2 % k == 0:  # also, if same remainder after adding to itself gets divided by k, just add count as one (same case of evenly divisble , 'remainder = 0' )
            count += 1
        else:
            count += maxCount  # if that is not the case, then we can add all the occurance of number having the remainder

    counter[
        maxIndex] = 0  # once we used the max remainder, set it to 0, to get the second max remainder occurance from the list,, till list's all value
print(
    count)  # i know the worst comments n explanation ever, but please deal with it :) because its my first explaination :D