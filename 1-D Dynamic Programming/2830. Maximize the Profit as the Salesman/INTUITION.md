# Intuition

- define dp[i]: the maximum profit ended at offers[i].end_time
- sort offers by end_time and we can use binary search

then for each offers[i], we can choose or skip
- if we skip, `dp[i] = dp[i-1]`
- if we choose, offers[i] can append after dp[j] where `dp[j].end_time < offers[i].start_time`

# Complexity
- Time complexity:

$$O(nlogn)$$

- Space complexity:

$$O(n)$$

# Code
```
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
```