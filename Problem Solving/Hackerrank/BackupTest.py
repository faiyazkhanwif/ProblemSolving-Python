from itertools import combinations
test_str = [1,7,2,4]
print("The original list is : " + str(test_str))

# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str))
       for j in range(i + 1, len(test_str) + 1)]
# printing result
print(res)
temp=[]
for i in range(len(res)):
    if len(res[i])>=2 and len(res[i])!=len(test_str):
        temp.append(res[i])
print(temp)
k=3
finalres=[]
for i in range(len(temp)):
    if len(temp[i])==2:
        if sum(temp[i])%k!=0:
            finalres.append(temp[i])
            print(str(i)+'= '+str(temp[i]))
    if len(temp[i])>2:
        count = 0
        for j in range(len(temp[i])):
            for m in range(len(temp[i])):
                if j!=m:
                    if temp[i][j]+temp[i][m]%k==0:
                        count=1
        if count==0:
            finalres.append(temp[i])
print(len(max(finalres)))