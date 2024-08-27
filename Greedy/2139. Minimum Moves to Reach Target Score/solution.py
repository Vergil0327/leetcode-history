class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while maxDoubles > 0 and target//2 > 0:
            res += 1 + target%2
            target //= 2
            maxDoubles -= 1

        return res + (target-1)
