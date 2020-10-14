#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
#code works but does not finish execution on time for some test cases.
def squares(a, b):
    count=0
    for i in range(a,b+1):
        res=math.sqrt(i)
        if res.is_integer()==True:
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

#Perfect solution using math formula from the discussions.
def squares(a, b):
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    return(sqrtB - sqrtA + 1)