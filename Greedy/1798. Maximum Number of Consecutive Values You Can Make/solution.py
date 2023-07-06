class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        res = 0
        for c in coins:
            if c > res+1: break
            res = res+c
        return res+1
