class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort(key=lambda x: x[1])

        j = 0
        for t in range(1, n + 1):
            dp[t] = dp[t-1]
            while j < len(rides) and t == rides[j][1]:
                start, end, tip = rides[j]
                dp[t] = max(dp[t], dp[start] + (end - start + tip))
                j += 1

        return dp[n]

from sortedcontainers import SortedDict
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x:x[1])

        dp = SortedDict()
        for start, end, tip in rides:
            i = dp.bisect_right(start)
            i -= 1

            j = dp.bisect_right(end)
            j -= 1
            dpPrev = dp.peekitem(j)[1] if j >= 0 else 0

            if i >= 0:
                _, accu = dp.peekitem(i)
                dp[end] = max(dpPrev, dpPrev, dp.get(end, 0), accu + end-start+tip)
            else:
                dp[end] = max(dpPrev, dp.get(end, 0), end-start+tip)

        return max(dp.values())
