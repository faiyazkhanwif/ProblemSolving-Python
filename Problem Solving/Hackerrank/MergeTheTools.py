#Medium problem, perfectly goes through all test cases
def merge_the_tools(string, k):
    n = len(string)
    i = 0
    count = 0
    temp = ''
    templist = []
    while i != n:
        temp += string[i]
        count += 1
        if count == k:
            templist.append(temp)
            count = 0
            temp = ''
        i += 1
    for i in range(len(templist)):
        temp1 = list(templist[i])
        anstmp = ''
        for j in range(len(temp1)-1,-1,-1):
            if temp1.count(temp1[j])>1:
                temp1.pop(j)
            else:
                anstmp+=str(temp1[j])
        finans = anstmp[::-1]
        print(finans)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)