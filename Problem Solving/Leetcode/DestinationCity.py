class Solution:
    def destCity(arr1):
        st = []
        des = []
        for i in range(len(arr1)):
            st.append(arr1[i][0])
            des.append(arr1[i][1])
        # print(st)
        # print(des)
        for i in range(len(des)):
            if des[i] not in st:
                return des[i]


res = Solution.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
print(res)
