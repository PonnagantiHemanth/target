def removingduplicate(nums):
    n = len(nums)
    duplictecount = 0 
    for i in range (1,n):
        if (nums[i] != nums[duplictecount]):
            duplictecount += 1 
            nums[duplictecount] = nums[i] 
    return duplictecount+1

nums = [1, 1, 2,8,8,8,8,3]
sol = (removingduplicate(nums))
print(nums[:sol])

