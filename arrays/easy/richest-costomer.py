# https://leetcode.com/problems/richest-customer-wealth/
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = sum(accounts[0])
        for i in range(1, len(accounts)):
            new_richest = sum(accounts[i])
            if new_richest > richest:
                richest = new_richest
        return  richest
