#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dop = 256
    days = 0
    if year%400 == 0 or (year%4==0 and year%100!=0):
        days = 244
    else:
        days = 243
    date = dop-days
    return(str(date)+'.09.'+str(year))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
