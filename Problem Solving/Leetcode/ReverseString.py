def rv(s):
    n = len(s)
    for i in range(int(n/2)):
        temp = s[i]
        temp1 = s[n - 1 - i]
        s[i] = temp1
        print(s[i])
        s[n - 1 - i] = temp
    print(s)
rv(["h","e","l","l","o"])