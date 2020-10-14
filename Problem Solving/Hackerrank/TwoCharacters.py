#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
#Shesh hoy nai, really hard problem
def alternate(s):
    ans = s
    for i in range(len(s)):
        print(s[i])
        if s.count(s[i])<2:
            ans= ans.replace(s[i],'')
            print(ans)
        elif s.count(s[i])>=2 and i!=len(s)-1:
            if s[i]==s[i+1]:
                ans=ans.replace(s[i],'')
                print(ans)
            else:
                print(ans)
    print(ans)
if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)

