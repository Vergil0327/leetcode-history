class Solution:
    def maxJump(self, stones: List[int]) -> int:
        res = stones[1]-stones[0]
        n = len(stones)
        
        for i in range(1, n-1):
            res = max(res, stones[i+1]-stones[i-1])
        return res