a = [2,7,11,15]
target = 9 
seen = {} 
l = len(a) 
for i in range (l):
    diff = target-a[i] 
    if (diff in seen):
        print([seen[diff],i])
    seen[a[i]] = i 
