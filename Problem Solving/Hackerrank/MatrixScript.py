
#!/bin/python3

import math
import os
import random
import re
import sys
#Hard problem, requires to do it without if-else statement.
def matrixscript(matrix,m):
    col1=0
    temp1=''
    for o in range(m):
        for p in range(len(matrix)):
            temp1+=matrix[p][col1]
        col1+=1
    ans = ''
    symcount = 0
    tp = ''
    for i in range(len(temp1)):
        if temp1[i].isalnum()==True:
            if symcount>0:
                ans+=' '
            ans+=temp1[i]
            symcount=0
            tp=''
        if temp1[i].isalnum()!=True:
            symcount+=1
            tp+=temp1[i]
        if i==len(temp1)-1:
            ans+=tp
    print(ans)

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrixscript(matrix,m)

#solution
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))