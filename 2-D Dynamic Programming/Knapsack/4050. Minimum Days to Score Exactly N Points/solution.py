"""
Optimal $O(N \sqrt{N})$ Unbounded Knapsack Solution

Since every streak of length $L$ adds $\frac{L(L + 1)}{2}$ points and takes $L$ days (plus $1$ mandatory skip day before starting the next streak), we can model this as an Unbounded Knapsack Problem:

1. Items (Streak Lengths):
A streak of length $L$ contributes $v_L = \frac{L(L+1)}{2}$ points and costs $c_L = L + 1$ days (accounting for the trailing skip day).
Since $v_L \le N$, $L$ only needs to go up to $\approx \sqrt{2N} \approx 450$.

2. DP State:
dp[s] = Minimum days (including trailing skips) required to achieve a score of exactly s.
- dp[0] = 0
- Transition: dp[s] = min(dp[s], dp[s - v_L] + (L + 1)) for all valid $L$.

3. Final Answer Adjustment:
The last streak does not require a trailing skip day, so we subtract $1$ from the final cost:$$\text{ans} = \text{dp}[N] - 1$$


Complexity Analysis:
- Time Complexity: O(N * sqrt(N)), where N <= 10^5. Number of items ≈ sqrt(2 * 10^5) ≈ 450. Inner loop runs N times. Total ops ≈ 450 * 10^5 = 4.5 * 10^7, completing in ~0.05 seconds.
- Space Complexity: O(N) for the 1D DP table.
"""
# Algorithm Approach:
# 1. Generate all useful streak lengths L such that v_L = L * (L + 1) // 2 <= N.
#    The maximum L is around sqrt(2 * 10^5) ≈ 450.
# 2. Initialize dp array of size N + 1 with infinity (INF), dp[0] = 0.
# 3. For each streak length L (with points v_L and day cost L + 1):
#      For s from v_L to N:
#        dp[s] = min(dp[s], dp[s - v_L] + L + 1)
# 4. Return dp[N] - 1 (subtracting 1 for the final unnecessary skip day).

class Solution:
    def minDays(self, n: int) -> int:
        # dp[s] = minimum days (including trailing skip day) to score 's' points
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute possible streak lengths L
        L = 1
        items = []
        while True:
            points = L * (L + 1) // 2
            if points > n:
                break
            days_cost = L + 1  # L days of earning + 1 day of trailing skip
            items.append((points, days_cost))
            L += 1
            
        # Unbounded Knapsack DP
        for points, cost in items:
            for s in range(points, n + 1):
                if dp[s - points] != float('inf'):
                    dp[s] = min(dp[s], dp[s - points] + cost)
                    
        # Subtract 1 because the final streak doesn't require a trailing skip day
        return dp[n] - 1
