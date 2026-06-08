"""
Since $n \le 1000$ and we have at most $m \le n$ subarrays, a naive DP transition would take $O(n \cdot m \cdot (r - l + 1))$, resulting in an $O(n^3)$ time complexity, which is too slow or right on the edge for a LeetCode Hard.
Hint 3 points out that we can optimize the inner lookup to $O(1)$ using a sliding window technique, dropping our overall runtime to a blazing fast $O(n \cdot m)$.

Let $dp[c][i]$ be the maximum sum of choosing at most $c$ subarrays using only the first $i$ elements of nums (1-indexed).
For each element $i$, we have two choices:

1. Do not end a subarray at $i$: The value is simply carried over from the previous index: $dp[c][i-1]$.
2. End a subarray at $i$: The subarray must start at some index $j$ such that its length is valid ($l \le i - j \le r$). The sum of this subarray is $P[i] - P[j]$, where $P$ is the prefix sum array.

The transition formula is:$$dp[c][i] = \max \left( dp[c][i-1], \ \max_{i-r \le j \le i-l} \{ dp[c-1][j] + P[i] - P[j] \} \right)$$

We can factor out $P[i]$ since it doesn't depend on $j$:$$dp[c][i] = \max \left( dp[c][i-1], \ P[i] + \max_{i-r \le j \le i-l} \{ dp[c-1][j] - P[j] \} \right)$$

For a fixed $c$ and an increasing $i$, the valid range for $j$ forms a sliding window of size $[i-r, i-l]$. We can maintain the maximum value of $(dp[c-1][j] - P[j])$ inside this window using a decreasing deque.
"""
from collections import deque
from typing import List

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        
        # 1-indexed Prefix Sum Array
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            
        # dp[c][i]: max sum using at most 'c' subarrays from the first 'i' elements.
        # Initialize with -inf because nums can contain large negative numbers.
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: 0 subarrays chosen yields a sum of 0
        for i in range(n + 1):
            dp[0][i] = 0
            
        # Global variable to track the max sum found (since we must pick at least 1 subarray)
        max_total_sum = float('-inf')
        
        # Iterate through the number of subarrays we can pick
        for c in range(1, m + 1):
            # Deque stores indices 'j' to optimize finding max(dp[c-1][j] - P[j])
            # It will maintain values in a strictly decreasing order.
            dq = deque()
            
            for i in range(1, n + 1):
                # 1. Carry over the best result from the left (not picking a subarray ending at i)
                dp[c][i] = dp[c][i - 1]
                
                # 2. Add the newly available index 'j = i - l' into our sliding window consideration
                j_to_add = i - l
                if j_to_add >= 0 and dp[c - 1][j_to_add] != float('-inf'):
                    val_to_add = dp[c - 1][j_to_add] - P[j_to_add]
                    # Maintain monotonic decreasing property in the deque
                    while dq and (dp[c - 1][dq[-1]] - P[dq[-1]]) <= val_to_add:
                        dq.pop()
                    dq.append(j_to_add)
                
                # 3. Evict indices from the front of the deque that have fallen out of the [i - r] window boundary
                if dq and dq[0] < i - r:
                    dq.popleft()
                
                # 4. If the deque is not empty, the front element provides the optimal 'j'
                if dq:
                    best_j = dq[0]
                    dp[c][i] = max(dp[c][i], P[i] + dp[c - 1][best_j] - P[best_j])
                    
                # Update our global maximum answer across all valid combinations
                max_total_sum = max(max_total_sum, dp[c][i])
                
        return max_total_sum