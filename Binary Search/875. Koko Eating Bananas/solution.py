class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            k = 0
            for p in piles:
                # k += ceil(p/speed)
                k += (p+(speed-1))//speed
            return k <= h

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l)//2
            if canFinish(mid):
                r = mid
            else:
                l = mid+1
        return l