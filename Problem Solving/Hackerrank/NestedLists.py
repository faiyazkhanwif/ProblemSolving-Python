if __name__ == '__main__':
    temp = []
    lm = []
    for _ in range(int(input())):
        ls = []
        name = input()
        score = float(input())
        ls.append(score)
        ls.append(name)
        lm.append(ls)
        temp.append(score)
    temp2 = list(dict.fromkeys(temp))
    temp2.sort()
    #print(temp2)
    lm.sort()
    #print(lm)
    key = temp2[1]
    #print(key)
    for i in range(len(lm)):
        if lm[i][0] == key:
            print(lm[i][1])
