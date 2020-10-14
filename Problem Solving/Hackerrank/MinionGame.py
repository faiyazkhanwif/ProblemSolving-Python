#Working code but runtime issues with long inputs
def minion_game(string):
    test_str = string
    res = [test_str[i: j] for i in range(len(test_str))
        for j in range(i + 1, len(test_str) + 1)]
    temp = []
    temp2 = []
    for i in range (len(res)):
        if res[i][0] in 'aeiou' or res[i][0] in 'AEIOU':
            temp.append(res[i])
        else:
            temp2.append(res[i])
    temp = list(dict.fromkeys(temp))
    temp2=list(dict.fromkeys(temp2))
    kevin=0
    stuart = 0
    for i in range(len(temp)):
        countkev = res.count(temp[i])
        kevin+=countkev
    for i in range(len(temp2)):
        countst = res.count(temp2[i])
        stuart+=countst

    if kevin>stuart:
        print('Kevin',kevin)
    elif kevin==stuart:
        print('Draw')
    else:
        print('Stuart',stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)

#pythonic perfect solution
def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")