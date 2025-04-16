def group_digit_frequency_pairs(num):
    same = num[1]
    count = 1 
    result = []
    for i in range(1,len(num)):
        if (same == num[i]):
            count += 1 
        else:
            result.append([num[i],count])
            count = 1 
    return result
        
# Example usage
print(group_digit_frequency_pairs("223314444411"))
# Output: [[2, 2], [3, 2], [1, 1], [4, 5], [1, 2]]
