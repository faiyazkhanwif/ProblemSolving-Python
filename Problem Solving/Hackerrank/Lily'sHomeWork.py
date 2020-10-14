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


if __name__ == '__main__':
    n  = int(input())
    arr = list(map(int, input().rstrip().split()))
    ans = quicksort(arr)
    print(z)
