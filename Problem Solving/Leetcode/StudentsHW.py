def sthw(arr1,arr2,q):
    count = 0
    for i in range(len(arr1)):
        if q>=arr1[i] and q<=arr2[i]:
            count+=1
    return count