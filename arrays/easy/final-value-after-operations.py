# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        options = {
            "X": 0,
            "X++": 1,
            "++X": 1,
            "--X": -1,
            "X--": -1,
        }
        counter = 0

        for i in operations:
            counter += options[i]
        return counter

sol = Solution()

print(sol.finalValueAfterOperations(["--X","X++","X++"]))
print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))