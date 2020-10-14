import sys

import itertools

#Brute force
def sub_lists(list1):
    # store all the sublists
    sublist = [[]]
    if len(list1)==1:
        return list1[0]
    else:
        temp = -sys.maxsize-1
        n = len(list1)
        indices = list(range(n + 1))
        for i, j in itertools.combinations(indices, 2):
            ans = list1[i:j]
            if sum(ans)>temp:
                temp = sum(ans)
        return (temp)



# driver code
l1 = [-2,1,-3,4,-1,2,1,-5,4]
print(sub_lists(l1))


#kadane's algorithm
def sub_lists(list1):
    # store all the sublists
    if len(list1)==1:
        return list1[0]
    else:
        #lowest possible number
        ans = -sys.maxsize-1
        #algorithm
        a=0
        for i in range(len(list1)):
            a+=list1[i]
            ans = max(a,ans)
            a= max(a,0)
        return ans

