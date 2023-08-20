class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x:x[1])
        m = len(offers)
        dp = [-inf] * m
        for i in range(m):
            dp[i] = max(dp[i], dp[i-1] if i-1 >= 0 else 0)
            j = bisect.bisect_left(offers, offers[i][0], key=lambda x:x[1])-1
            dp[i] = max(dp[i], (dp[j] if j >= 0 else 0) +offers[i][2])
            
        return dp[-1]