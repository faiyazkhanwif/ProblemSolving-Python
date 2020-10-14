n, m = input().split()
n = int(n)
m = int(m)
sc_ar = input().split()
A = set(input().split())
B = set(input().split())
count=0
for i in range(len(sc_ar)):
    if sc_ar[i] in A:
        count+=1
    if sc_ar[i] in B:
        count-=1
print(count)


#short solution
#print(sum([(i in A) - (i in B) for i in sc_ar]))