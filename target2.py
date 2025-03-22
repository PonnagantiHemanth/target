def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st = end = poi = 0
    
    for i in range(size):
        curr_sum += arr[i]
        
        if max_so_far < curr_sum:
            max_so_far = curr_sum
            st = poi
            end = i
        
        if curr_sum < 0:
            curr_sum = 0
            poi = i + 1
    
    print("Maximum sum Subarray is", max_so_far)
    print("Start Index of window is", st)
    print("End Index of window is", end)
    
    return max_so_far, st, end

# Example usage:
v = max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Result:", v)
