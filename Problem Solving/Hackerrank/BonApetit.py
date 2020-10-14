#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    noteat = bill[k]
    totbill = 0
    annabill = 0
    for i in range(len(bill)):
        totbill+=bill[i]
    annabill = (totbill/2)-(noteat/2)
    if annabill == b:
        print("Bon Appetit")
    else:
        print(int(b-annabill))
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
