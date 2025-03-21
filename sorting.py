def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                print(arr)
    return arr

# Example usage
arr = [5, 3, 8, 1, 2]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 5, 8]
