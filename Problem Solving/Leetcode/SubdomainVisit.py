def subdm(arr1):
    tempalph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'
                ,'x','y','z','.']
    points = []
    domain = []
    subdomain = []
    allsubdomain = []
    #print(arr1)
    for i in range(len(arr1)):
        temp = ''
        temp2 = ''
        for j in range(len(arr1[i])):
            if arr1[i][j] not in tempalph and arr1[i][j]!=' ' and arr1[i][j]!='.':
                temp+=arr1[i][j]
            if arr1[i][j] in tempalph and arr1[i][j] != ' ':
                temp2 += arr1[i][j]
        points.append(int(temp))
        domain.append(temp2)
    for i in range(len(domain)):
        tmpdm = []
        tmpdm.append(domain[i])
        allsubdomain.append(domain[i])
        for j in range(len(domain[i])):
            if domain[i][j]=='.':
                tmpdm2 = ''
                for k in range(j+1,len(domain[i])):
                    tmpdm2+=domain[i][k]
                tmpdm.append(tmpdm2)
                allsubdomain.append(tmpdm2)
        subdomain.append(tmpdm)
    tempalph=[]
    count = []
    for i in range(len(allsubdomain)):
        if allsubdomain[i] not in tempalph:
            tempalph.append(allsubdomain[i])
            count.append(0)
    #print(points)
    #print(domain)
    #print(subdomain)
    #print(allsubdomain)
    #print(tempalph)
    #print(count)
    for i in range(len(tempalph)):
        for j in range(len(subdomain)):
            if tempalph[i] in subdomain[j]:
                count[i]+=points[j]
    for i in range(len(count)):
        count[i]=str(count[i])
        count[i]+=' '
        count[i]+=tempalph[i]
    return count


result = subdm(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(result)


#most efficient solution from discussion using hash:
def subdomainVisits(cpdomains):
    hashmap = {}
    for cpdom in cpdomains:
        (num, domain) = (int(x) if i == 0 else x for i, x in enumerate(cpdom.split(" ")))
        domains = domain.split('.')  # split the domain by '.'
        for idx in reversed(range(len(domains))):
            subdomain = '.'.join(domains[idx:])
            val = hashmap.get(subdomain, 0)  # 0 if not found in hashmap
            val += num
            hashmap[subdomain] = val

    # print(hashmap)
    ans = []
    for subdomain, count in hashmap.items():
        ans.append(" ".join([str(count), subdomain]))  # join count and subdomain using empty space (" ")

    return ans