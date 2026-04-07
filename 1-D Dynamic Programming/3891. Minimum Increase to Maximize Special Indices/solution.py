"""
first of all, a "special index" is essentially a local peak. => no two special indices can be adjacent. This means if index $i$ is special, index $i-1$ and $i+1$ cannot be
This "neighbor exclusion" property makes it a classic House Robber style DP, but with a twist: each "choice" (making an index a peak) has a specific cost.

1. The Cost of Making a Peak

To make nums[i] a special index, it must be strictly greater than nums[i-1] and nums[i+1]. Since we can only increase values:
- nums[i] must become at least $\max(\text{nums}[i-1], \text{nums}[i+1]) + 1$.
- The cost to do this is $\max(0, \max(\text{nums}[i-1], \text{nums}[i+1]) + 1 - \text{nums}[i])$.

2. DP State Definition

As the hint suggests, we store a pair at each step: dp[i] = (max_peaks, min_ops).

- max_peaks: The maximum number of special indices we've created up to index $i$.
- min_ops: The minimum operations to get that many peaks.

Rule: higher peaks are always better; if peaks are equal, lower operations are better.

3. State Transition

For each index $i$ (from $1$ to $n-2$), we have two choices:

- Choice A: Skip index $i$: The state is simply inherited from $i-1$. $$(peaks, ops) = dp[i-1]$$
- Choice B: Make index $i$ a peak: This index becomes a peak. Because $i-1$ cannot be a peak, we must look at the result from $i-2$. $$cost = \max(0, \max(nums[i-1], nums[i+1]) + 1 - nums[i])$$$$(peaks, ops) = (dp[i-2].peaks + 1, dp[i-2].ops + cost)$$
"""
class Solution:
    def minIncrease(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i] = (max_special_indices, min_operations)
        # We only need the last two states (i-1 and i-2), so we can use variables.
        
        # Initial states
        prev2 = (0, 0) # dp[i-2] (starts at index -1, which is effectively 0 peaks, 0 ops)
        prev1 = (0, 0) # dp[i-1] (starts at index 0, which can't be a special index)
        
        for i in range(1, n - 1):
            # Choice 1: Don't make i a special index
            res_skip = prev1
            
            # Choice 2: Make i a special index
            # Cost to make nums[i] > nums[i-1] AND nums[i] > nums[i+1]
            target = max(nums[i-1], nums[i+1]) + 1
            cost = max(0, target - nums[i])
            res_make = (prev2[0] + 1, prev2[1] + cost)
            
            # Update current state based on max peaks, then min cost
            if res_make[0] > res_skip[0]:
                current = res_make
            elif res_make[0] < res_skip[0]:
                current = res_skip
            else:
                current = (res_make[0], min(res_make[1], res_skip[1]))
            
            # Shift states forward
            prev2 = prev1
            prev1 = current
            
        return prev1[1]