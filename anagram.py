a = ['cat','dog','god','tca','act']
for i in range(len(a)):
    v = ''.join(sorted(a[i]))
    a[i] = v 


print(a)
dic = {}
for i in range(len(a)):
    if (a[i] in dic):
        dic[a[i]] +=  [i] 
    else:
        dic[a[i]] = [i] 
print(dic) 