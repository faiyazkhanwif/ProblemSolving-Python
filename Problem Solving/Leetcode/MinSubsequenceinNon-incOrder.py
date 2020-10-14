def minsubord(arr1):
    target = sum(arr1)
    temp = 0
    ans = []
    arr1.sort()
    while temp <= target:
        temp += arr1[-1]
        ans.append(arr1[-1])
        target = target-arr1[-1]
        arr1.pop()
    return ans


result = minsubord([6])
print(result)