# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or val is None:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
            print(nums)

        return len(nums)


solutionTest = Solution().removeElement([0,1,2,2,3,0,4,2], 2)
# solutionTest = Solution().removeElement([3,2,2,3], 3)
print(solutionTest)

