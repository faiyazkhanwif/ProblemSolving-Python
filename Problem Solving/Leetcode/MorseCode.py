from collections import Counter
def morse(arr1):
    arr2 = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
            ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    ans = []
    for i in range(len(arr1)):
        tempword = ''
        for j in range(len(arr1[i])):
            temp = words.index(arr1[i][j])
            tempword += arr2[temp]
        ans.append(tempword)
    return len(list(Counter(ans).values()))


print(morse(["gin", "zen", "gig", "msg"]))
