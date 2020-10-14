#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
#Got 16 points out of 20.
def repeatedString(s, n):
    length = len(s)
    counta = s.count('a')
    if counta == length:
        return n
    if n>length and n%length==0:
        countans = (n/length)*counta
        return int(countans)
    if n>length and n%length!=0:
        temp = int(n/length)
        temp1 = (n/length)-temp
        temp2 = (temp1*length)
        print(temp2)
        if temp2>0.90:
            temp2=math.ceil(temp2)

        templist=''
        for i in range(int(temp2)):
            templist+=s[i]
        counta2 = templist.count('a')
        countans = temp*counta+counta2
        return (countans)
if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)


#Pythonic solution
s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
