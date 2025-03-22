def permute(string, step=0):
    if (step == len(string)):
        print(''.join(string))
        return 
    for i in range (step,len(string)):
        string[step],string[i] = string[i],string[step]
        permute(string,step + 1) 
        string[step],string[i] = string[i],string[step]

# Example usage
word = "hemanth"
permute(list(word))
