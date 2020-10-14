class Solution:
    def runningSum(arr):
        temp = 0
        for i in range(len(arr)):
            arr[i]=arr[i]+temp
            temp=arr[i]
        return arr
if __name__ == '__main__':
    arr = input()
    arr = arr.replace(',','')
    arr = arr.replace('[','')
    arr = arr.replace(']','')
    #print(arr)
    arr1=[]
    for i in range(len(arr)):
        arr1.append(int(arr[i]))
    #print(arr1)
    result = Solution.runningSum(arr1)

    print(result)