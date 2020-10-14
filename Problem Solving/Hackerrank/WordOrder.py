#Medium problem. fails 3 testcases because of timeout
def wordorder(inps):
    temp = []
    ans = ''
    for i in range(len(inps)):
        if inps[i] not in temp:
            temp.append(inps[i])
            countw = inps.count(inps[i])
            ans = ans + str(countw) + ' '
    print(len(temp))
    print(ans)

if __name__ == '__main__':
    inps = []
    n = input()
    for i in range(int(n)):
        s = input()
        inps.append(s)
    res = wordorder(inps)

#Efficient Solution
from collections import OrderedDict
words = OrderedDict()
for i in range(int(input())):
    eachword = input().strip()
    words[eachword] = words.get(eachword, 0) + 1
print (len(words))
print (*words.values())