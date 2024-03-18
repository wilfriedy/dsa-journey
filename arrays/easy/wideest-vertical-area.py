# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[0])
        maxWidth = 0

        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            maxWidth = max(maxWidth, width)
        return maxWidth


sol = Solution()
print(sol.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))