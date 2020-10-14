def twosum(tar,arr):
    ans = []
    for i in range(len(arr)):
        temp = tar-arr[i]
        arr[i]=9.99
        if temp in arr:
            ans.append(i)
            ans.append(arr.index(temp))
            break
    print(ans)

twosum(-1,[0,3,-3,4,-1])