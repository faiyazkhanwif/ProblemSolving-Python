def rs(st):
    temp = ''
    ans = ''
    for i in range(len(st)):
        if i == len(st) - 1:
            temp += st[i]
            temp = temp[::-1]
            ans += temp
        elif st[i] == ' ':
            temp = temp[::-1]
            ans += temp
            ans += ' '
            temp = ''
        else:
            temp += st[i]
    return ans


print(rs("Let's take LeetCode contest"))
