def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    equal = [pivot]
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        if arr[i] > pivot:
            right.append(arr[i])
    result = quicksort(left) + equal + quicksort(right)
    print(*result)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    quicksort(arr)
