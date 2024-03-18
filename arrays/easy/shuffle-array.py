# https://leetcode.com/problems/shuffle-the-array/description/
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k = n-1
        j = k + 1
        i = 0
        while i < n:
            # print(j)
            if i == k:
                print('hh', i)
                nums[i],nums[i+1] = nums[i+1], nums[i]
                break
            else:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                print(nums)
            j += 1
            i += 1
        return nums


# second attempt
class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j = (n*2) - 2
        while j > n :
            if j == n:
                nums[n-2], nums[j] = nums[j], nums[n-2]
                print(nums, 'endinggggggg')
            else:
                nums[n-1], nums[j] = nums[j], nums[n-1]
                print(nums, f'when j = {j}')
            j -= 1
        return nums






# sol = Solution()
# print(sol.shuffle([2,5,1,3,4,7], 3))
sol = Solution2()
print(sol.shuffle([2,5,1,3,4,7], 3))
# print(sol.shuffle([1,2,3,4,4,3,2,1], 4))