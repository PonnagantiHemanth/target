n =20
for i in range (1,n+1):
    for j in range (1,n+i):
        if (j <= n-i):
            print(" ",end = '')
        else:
            print("*",end = '')
    print()


    n = 5  # Number of rows
sol = []

for i in range(1, n + 1):
    row = ""
    for j in range(1, n + i):
        if j <= n - i:
            row += " "  # Append spaces
        else:
            row += "*"  # Append stars
    sol.append(row)  # Store the row in the list
    print(row)  # Print the row immediately

# If you want to print stored rows later:
print("\nStored Rows:")
for row in sol:
    print(row)
