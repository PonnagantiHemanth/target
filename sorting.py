from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Two-pointer approach (in-place modification)
        unique_index = 0  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        return unique_index + 1  # Return the new length
v = Solution()
vo = v.removeDuplicates([1,1,2])
print(vo)