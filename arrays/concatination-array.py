# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #---- solution1
        # dble = len(nums) * 2
        # for i in nums:
        #    if len(nums) == dble:
        #         break
        #    nums.append(i)
        # return nums
        #---- solution2
        return nums * 2

sol = Solution()
print(sol.getConcatenation([1,2,1]))