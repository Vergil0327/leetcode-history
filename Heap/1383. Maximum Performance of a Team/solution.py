class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = int(1e9+7)
        arr = sorted(zip(speed, efficiency), key=lambda x:-x[1])

        pq = []
        currSpeedSum = 0
        res = 0
        for spd, eff in arr:
            heapq.heappush(pq, spd)
            currSpeedSum += spd

            if len(pq) > k:
                currSpeedSum -= heapq.heappop(pq)

            res = max(res, currSpeedSum * eff)
        return res % MOD