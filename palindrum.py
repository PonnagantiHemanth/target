a = ("A man, a plan, a canal, Panama") 
s = ''
for i in a:
    if (i.isalpha() or i.isdigit()):
        s += i.lower()
v = s[::-1]
print(v == s)