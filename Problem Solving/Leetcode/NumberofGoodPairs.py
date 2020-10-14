class Solution:
    def numIdenticalPairs(arr):
        i = 0
        j = 1
        ans = []
        while i < len(arr) - 1:
            if arr[i] == arr[j] and i < j:
                ans.append((i, j))
            if j == len(arr) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        return len(ans)


result = Solution.numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(result)