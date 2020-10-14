#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
#Medium problem, got 12 points out of 20. 4 test cases did not solve because of timeout.
def climbingLeaderboard(scores, alice):
    scorespos=[]
    position = []
    count=0
    for i in range(len(scores)):
        if i==0:
            count+=1
            scorespos.append(count)
        if i > 0:
            if scores[i]!=scores[i-1]:
                count+=1
                scorespos.append(count)
            elif scores[i]==scores[i-1]:
                scorespos.append(count)
    for i in range (len(alice)):
        for j in range (len(scores)):
                if alice[i] < scores[j]:
                    if j != len(scores) - 1:
                        continue
                    elif j == len(scores)-1:
                        position.append(scorespos[j]+1)
                        break
                elif alice[i] > scores[j]:
                    position.append(scorespos[j])
                    break
                elif alice[i] == scores[j]:
                    position.append(scorespos[j])
                    break
    return position
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#Solution for all test cases
def climbingLeaderboard(scores, alice):
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores)-1
    while score_index!=len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index>-1:
            highscore_index-=1
            if scores[highscore_index]!=scores[highscore_index+1]:
                currentrank-=1
        if alice[score_index] == scores[highscore_index]:
            yield currentrank
        else:
            yield currentrank+1
        score_index+=1