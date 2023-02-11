class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(currSpeed):
            timeTakes = 0
            for i, d in enumerate(dist):
                if i < len(dist)-1:
                    timeTakes += ceil(d/currSpeed)
                else:
                    timeTakes += d/currSpeed
            return timeTakes <= hour

        l, r = 1, int(1e7)
        if not check(r): return -1

        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l
          
