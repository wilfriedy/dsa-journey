#https://leetcode.com/problems/find-words-containing-character/
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]

sol = Solution()

print(sol.findWordsContaining(["leet","code"], 'e'))