class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        presum1 = list(accumulate(grid[0], initial=0))
        presum2 = list(accumulate(grid[1], initial=0))

        # robot1 turning down at i-th grid
        res = presum1[n] + presum2[n]
        for i in range(n):
            top_remain = presum1[n]-presum1[i+1]
            bottom_remain = presum2[i]
            res = min(res, max(top_remain, bottom_remain))
        return res