class Solution:
    def shuffle(n,arr):
        print(arr)
        ans=[]
        for i in range(n):
            ans.append(arr[i])
            ans.append(arr[i+n])
        return ans

print(Solution.shuffle(3,[2,5,1,3,4,7]))
