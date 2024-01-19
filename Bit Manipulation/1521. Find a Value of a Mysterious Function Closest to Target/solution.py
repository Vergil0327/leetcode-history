class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        dp = set()
        res = inf
        for num in arr:
            nxt = set([num])
            for best in dp:
                nxt.add(num & best)
            
            for best in nxt:
                res = min(res, abs(best-target))
            dp = nxt
        return res
