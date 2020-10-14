#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    countk1 = x1
    countk2 = x2
    countf = 0
    if  x1 <= 10000 and v1 <= 10000:
        while countk1<=21474836 and countk2<=21474836:
            countk1+=v1
            countk2+=v2
            if countk1==countk2:
                countf+=1
                break
    if countf>0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
