a = [1,2,3]
b = 3
c = len(a)
s = (c%b)
print(s)
print(a[s:] + a[:s])
