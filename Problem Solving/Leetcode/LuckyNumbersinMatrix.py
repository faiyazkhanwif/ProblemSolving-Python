def luckymat(arr1):
    temp = []
    n = len(arr1) * len(arr1[0])
    h = 0
    j = 0
    t = []
    ans=[]
    for i in range(n):
        t.append(arr1[h][j])
        h += 1
        if h == len(arr1):
            h = 0
            j += 1
            temp.append(t)
            t = []
    #print(temp)
    for i in range(len(arr1)):
        mini = min(arr1[i])
        ind = arr1[i].index(mini)
        if mini == max(temp[ind]):
            ans.append(mini)
    return ans



print(luckymat([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
