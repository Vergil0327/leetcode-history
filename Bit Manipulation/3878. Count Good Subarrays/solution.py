"""
**Bitwise OR problems on subarrays usually have a specific "intuition" anchor:**

The bitwise OR of a subarray is non-decreasing as you expand it.
Even more importantly, for any fixed starting point $i$, as you increase $j$, the value of nums[i] | ... | nums[j] can only change at most 30 times (since each change must set at least one new bit to 1).

The fundamental property to track is: For a subarray nums[i...j], is the current cumulative OR value equal to any element that has appeared between index i and j?

The Correct Intuition: The "Last Occurrence" Map

Because the bitwise OR of a subarray nums[i...j] only changes at most 30 times as we move i to the left (for a fixed j), we can divide the starting positions i into at most 31 intervals. In each interval, the OR value is constant.
For each interval, we just need to check: Is the constant OR value present in nums[i...j]?
The most efficient way to check this is to see if the last seen position of that OR value is $\ge i$.
"""

class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        last_pos = {}  # Tracks the last index of every number seen so far
        # List of [or_value, leftmost_index_with_this_or]
        # ordered from right-to-left (j down to 0)
        dp = [] 
        total_good = 0

        for j in range(n):
            val = nums[j]
            last_pos[val] = j
            
            # 1. Update OR intervals for the new element at j
            next_dp = [[val, j]]
            for or_val, start_idx in dp:
                new_or = or_val | val
                if new_or == next_dp[-1][0]:
                    # Keep the leftmost start_idx for the same OR value
                    next_dp[-1][1] = start_idx
                else:
                    next_dp.append([new_or, start_idx])
            dp = next_dp
            
            # 2. Count start positions 'i' that make a good subarray ending at j
            # Each element in dp is [OR_value, start_idx]
            # It represents an interval of i: [dp[k][1], dp[k-1][1]-1]
            for k in range(len(dp)):
                current_or = dp[k][0]
                left_bound = dp[k][1]
                right_bound = dp[k-1][1] - 1 if k > 0 else j
                
                # Check if 'current_or' exists in nums[i...j]
                # If its last occurrence is >= i, then nums[i...j] is Good.
                if current_or in last_pos:
                    pos = last_pos[current_or]
                    # We need start_idx 'i' such that:
                    # left_bound <= i <= right_bound AND i <= pos
                    if pos >= left_bound:
                        valid_end = min(right_bound, pos)
                        total_good += (valid_end - left_bound + 1)
        
        return total_good