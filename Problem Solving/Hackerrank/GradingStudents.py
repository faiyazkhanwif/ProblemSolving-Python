#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]>=0 and grades[i]<=100:
            if grades[i]<38:
                grades[i]
            elif grades[i]>=38:
                temp = grades[i]
                tempres = int(temp/5)
                tempres+=1
                possgrade = tempres*5
                diff = abs(temp-possgrade)
                print(diff)
                if diff<3:
                    grades[i] = int(possgrade)
                elif diff==3:
                    grades[i] = temp
                else:
                    grades[i] = temp
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
