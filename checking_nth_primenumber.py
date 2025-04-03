def prime(N):
    for i in range(2,int(N**0.5)+1):
        if (N%i == 0):
            return False 
    return True 
def Check(N):
    co = 0 
    num = 1 
    while (co < N):
        num += 1 
        if (prime(num)):
            co += 1 
    return num 
print(Check(5))