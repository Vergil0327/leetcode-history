"""
let dp[i][j] = the minimum cost to get exactly $j$ peaks using the first $i$ elements.

1. The Core Strategy: Breaking the Circle

In a circular array, the status of index $0$ affects both index $1$ and index $n-1$. To handle this, we split the problem into two distinct, linear scenarios:

Case 1: Index 0 is FORCED to be a Peak
- Cost: We calculate the cost to make nums[0] a peak: $C_0 = \max(0, \max(nums[n-1], nums[1]) + 1 - nums[0])$.
- Constraint: Since $0$ is a peak, its neighbors ($1$ and $n-1$) cannot be peaks.
- Sub-problem: We need to find $k-1$ more peaks in the remaining linear range $[2, n-2]$.

Case 2: Index 0 is FORBIDDEN from being a Peak
- Constraint: Index $0$ is just a regular element. It provides a boundary value for its neighbors but is never a peak itself.
- Sub-problem: We need to find $k$ peaks in the remaining linear range $[1, n-1]$. (Note: In this range, $1$ and $n-1$ are no longer "connected," so they are treated as the ends of a line).

2. The Linear DP Engine
For both cases, we need a function solve_linear(range, target_k) that finds the minimum cost to pick target_k non-adjacent peaks in a fixed line.

State Definition:
$dp[i][j]$ = The minimum cost to get exactly $j$ peaks using the first $i$ elements of the provided range.

Transitions:
For each element at position $i$ in the range:

1. Option 1 (Skip $i$): $dp[i][j] = dp[i-1][j]$
2. Option 2 (Make $i$ a Peak): $dp[i][j] = dp[i-2][j-1] + \text{cost}(i)$
    - Note: The $\text{cost}(i)$ is always calculated using the original neighbors from the circular array to ensure the "peak" definition remains valid.
"""

from math import inf

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == 0: return 0
        # In a circle, you can have at most floor(n/2) peaks
        if k > n // 2: return -1

        def get_cost(i):
            """Calculates cost to make nums[i] a peak based on original neighbors."""
            l = nums[(i - 1) % n]
            r = nums[(i + 1) % n]
            return max(0, max(l, r) + 1 - nums[i])

        def solve_linear(start, end, target_k):
            """Standard DP to find min cost for target_k peaks in a linear slice."""
            if target_k <= 0: return 0
            length = end - start + 1
            if length < 2 * target_k - 1: return inf
            
            # dp[i][j] = min cost using i elements to get j peaks
            dp = [[inf] * (target_k + 1) for _ in range(length + 1)]
            dp[0][0] = 0
            
            for i in range(1, length + 1):
                curr_real_idx = start + i - 1
                cost = get_cost(curr_real_idx)
                
                for j in range(target_k + 1):
                    # Choice 1: Don't make this index a peak
                    dp[i][j] = dp[i-1][j]
                    
                    # Choice 2: Make this index a peak
                    if j > 0:
                        # To pick i, we must have come from i-2
                        prev_cost = dp[i-2][j-1] if i >= 2 else (0 if j == 1 else inf)
                        if prev_cost != inf:
                            dp[i][j] = min(dp[i][j], prev_cost + cost)
            return dp[length][target_k]

        # Case 1: Index 0 is a peak. 
        # Range is [2, n-2] for the remaining k-1 peaks.
        res1 = get_cost(0) + solve_linear(2, n - 2, k - 1)
        
        # Case 2: Index 0 is NOT a peak. 
        # Range is [1, n-1] for all k peaks.
        res2 = solve_linear(1, n - 1, k)

        ans = min(res1, res2)
        return ans if ans < inf else -1