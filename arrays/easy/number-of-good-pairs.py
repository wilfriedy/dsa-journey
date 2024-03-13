# https://leetcode.com/problems/number-of-good-pairs/
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i= 0
        count = 0

        while i < len(nums):
            j = len(nums) - 1
            print([nums[i], nums[j]], 'comparing upper')
            while j > i:
                if nums[j] == nums[i]:
                    print([nums[i], nums[j]], 'comparing')
                    count += 1
                j -= 1
            i += 1
        return count



sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))