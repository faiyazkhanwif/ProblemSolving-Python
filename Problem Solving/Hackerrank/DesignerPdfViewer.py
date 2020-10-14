#!/bin/python3

import os


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    heightlist = []
    letterlist = []
    for i in range(ord('a'), ord('z') + 1):
        letterlist.append(chr(i))
    print(letterlist)
    for i in range(len(letterlist)):
        for j in range(len(word)):
            if letterlist[i] == word[j]:
                heightlist.append(h[i])
                print(word[j])
                break
    print(heightlist)
    maxheight = max(heightlist)
    neededheight = len(word) * 1 * maxheight
    return neededheight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
