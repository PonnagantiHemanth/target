def sub(sol):
    maximum = sol[0]
    minimum = sol[0]
    re = sol[0]
    for i in range (1,len(sol)):
        if (sol[i] < 0):
            maximum,minimum = minimum,maximum
        
        maximum = max(sol[i],maximum*sol[i])
        minimum = min(sol[i],minimum*sol[i])
        
    return max(re,maximum)


sol = [2,3,4,5,-6,-7]
print(sub(sol))
