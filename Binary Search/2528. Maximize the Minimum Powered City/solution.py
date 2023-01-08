class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def isValidPower(target):
            extra = k

            cityPower = sum(stations[:r]) # sliding window
            additional = [0] * n
            for i in range(n):
                if i+r<n:
                    cityPower += stations[i+r] + additional[i+r]
                if i-r-1>=0:
                    cityPower -= stations[i-r-1] + additional[i-r-1]

                if cityPower < target:
                    need = target - cityPower
                    if need > extra: return False

                    additional[min(n-1, i+r)] += need
                    extra -= need
                    cityPower = target

            return True

        lo, hi = 0, sum(stations) + k
        while lo < hi:
            mid = hi - (hi-lo)//2
            if isValidPower(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo