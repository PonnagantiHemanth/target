def Climb_stairs(n):
    step=(n+1)*[0]
    if(n==1 or n==2):
        return n
    step[1]=1
    step[2]=2
    for i in range(3,n+1):
        step[i]=step[i-1]+step[i-2]
    return step[n]

print(Climb_stairs(5))
