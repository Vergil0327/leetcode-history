class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k: return -1

        def canMake(days):
            adjacent = 0
            bouquets = 0
            for i in range(n):
                if bloomDay[i] <= days:
                    adjacent += 1
                    if adjacent == k:
                        bouquets += adjacent // k
                        adjacent = 0
                else:
                    adjacent = 0
            return bouquets >= m


        l, r = 0, max(bloomDay)
        while l < r:
            mid = l + (r-l)//2
            if canMake(mid):
                r = mid
            else:
                l = mid+1
        return l