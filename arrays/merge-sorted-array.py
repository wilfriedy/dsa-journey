# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_of_num1 = m-1
        end_of_num2 = n-1
        last_merged_end = m + n - 1

        while end_of_num2 >= 0:
            if end_of_num1 >= 0 and nums1[end_of_num1] > nums2[end_of_num2]:
                nums1[last_merged_end] = nums1[end_of_num1]
                end_of_num1 -= 1
            else:
                nums1[last_merged_end] = nums2[end_of_num2]
                end_of_num2 -= 1

            last_merged_end -= 1

        print(nums1)

sol = Solution()

print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))