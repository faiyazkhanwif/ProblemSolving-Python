#For calculating runtime, z is used.
z=-1
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    i = -1
    j = 0
    while j < len(arr):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
            global z
            z+=1
        elif arr[j] > pivot:
            j += 1
        else:
            j += 1
    arr.insert(i + 1, pivot)
    z+=1
    arr.pop(len(arr) - 1)
    arr = quicksort(arr[0:i + 1]) + [pivot] + quicksort(arr[i + 2:len(arr)])
    #print(arr)
    return arr
def insertionSort2(n, arr):
    ri=0
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i + 1] = arr[i]
            arr[i]=temp
            k=i
            ri+=1
            for j in range(i-1,-1,-1):
                if arr[j]>arr[k]:
                    temp1 = arr[j]
                    arr[j] = arr[k]
                    arr[k] = temp1
                    k=k-1
                    ri+=1
    #print(*arr)
    return ri

if __name__ == '__main__':
    n  = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr2=arr.copy()
    quicksort(arr)
    runi = insertionSort2(n, arr2)
    runq = z
    print(int(runi)-int(runq))
