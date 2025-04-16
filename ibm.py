def getMinimumOperations(arr):
    i, j = 0, len(arr) - 1
    ops = 0

    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] < arr[j]:
            arr[i + 1] += arr[i]
            i += 1
            ops += 1
        else:
            arr[j - 1] += arr[j]
            j -= 1
            ops += 1

    return ops

# Sample Input
arr = [2, 9, 7, 1, 4, 7]
print(getMinimumOperations(arr))  # Output: 3
