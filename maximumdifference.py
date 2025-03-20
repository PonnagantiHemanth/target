def fun(v):
    currentdiff = 0 
    sorting = sorted(v,reverse=False) 
    l = len(sorting)
    for i in range (l-1):
        if (sorting[i+1]-sorting[i] > currentdiff):
            currentdiff = sorting[i+1]-sorting[i]
    return currentdiff





v = [5,32,45,4,12,18,25]
print(fun(v))