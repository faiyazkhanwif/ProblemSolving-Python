def lcp(arr):
    if len(arr) == 0:
        return ''
    if len(arr) == 1:
        return arr[0]
    if len(arr[0]) == 0:
        return ''
    count = 0
    temp = arr[0][0]
    ans = ''
    smln = len(arr[0])
    for i in range(len(arr)):
        if len(arr[i]) == 0:
            return ''
        else:
            if arr[i][0] == temp:
                count += 1
            if len(arr[i]) < smln:
                smln = len(arr[i])
    if count > 1:
        ans += arr[0][0]
    else:
        return ''
    if count != len(arr):
        return ''
    for i in range(1, smln):
        temp1 = arr[0][i]
        count1 = 0
        for j in range(len(arr)):
            if arr[j][i] == temp1:
                count1 += 1
        if count1 == count:
            ans += temp1
    return ans


result = lcp(["apple", "apply", "app", "at"])
print(result)
