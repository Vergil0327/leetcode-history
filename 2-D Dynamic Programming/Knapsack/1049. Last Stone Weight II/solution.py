class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        
        dp = {0}
        for i in range(n):
            nxt = set()
            for SUM in dp:
                nxt.add(SUM+stones[i])
                nxt.add(SUM-stones[i])
            dp = nxt
        
        res = inf
        for weight in dp:
            if weight < 0: continue
            res = min(res, weight)
        return res
