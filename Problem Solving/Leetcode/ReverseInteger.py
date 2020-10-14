def reverseint(n):
    temp = str(n)
    if len(temp) == 1:
        return temp
    sign = ''
    ans = ''
    switch = 'off'
    if temp[0] == '-':
        sign = '-'
    for i in range(len(temp) - 1, -1, -1):
        if temp[i] == '-':
            break
        else:
            if temp[i] == '0' and switch == 'off':
                continue
            else:
                ans += temp[i]
                switch = 'on'
    # print(ans)
    # i = 0
    # for i in range(len(ans)):
    #    if ans[0]==0
    ans = sign + ans
    return ans


result = reverseint(6036000)
print(result)
