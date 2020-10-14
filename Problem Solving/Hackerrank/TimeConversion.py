#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.strip()
    #hour is first to digits
    hour = int(time[:2])
    #meridian is am pm indicator which is after 8th
    meridian = time[8:]
    # Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
    if (hour == 12):
        hour = 0
    if (meridian == 'PM'):
        hour += 12
    return("%02d" % hour + time[2:8])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
