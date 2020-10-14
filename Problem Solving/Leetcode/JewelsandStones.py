def jands(j, s):
    temp = []
    c = 0
    for i in range(len(j)):
        temp.append(j[i])
    for i in range(len(temp)):
        tmp = s.count(temp[i])
        c += tmp
    return c


print(jands('aA', 'aAAbbbb'))
