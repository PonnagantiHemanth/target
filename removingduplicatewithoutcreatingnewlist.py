from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_index = 0  # Pointer to track the last unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:  # If a new unique element is found
                unique_index += 1
                nums[unique_index] = nums[i]  # Move the unique element forward

        return unique_index + 1  # Return count of unique elements
nums = [1, 1, 2,8,8,8,8,3]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k)        # Output: 2
print(nums[:k]) # Output: [1, 2]
