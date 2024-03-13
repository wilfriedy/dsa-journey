# https://leetcode.com/problems/build-array-from-permutation/description/
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


solution = Solution()
print(solution.buildArray([0,2,1,5,3,4]))