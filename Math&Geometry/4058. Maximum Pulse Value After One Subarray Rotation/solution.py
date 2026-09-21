"""
Mathematical Insight:
The original pulse value is:
  pulse(nums) = sum_{i=0..n-1} (-1)^i * nums[i]

Let P[t] be the alternating prefix sum of the first t elements:
  P[0] = 0
  P[t] = sum_{i=0..t-1} (-1)^i * nums[i]

When we left-rotate nums[l..r] by 1 position:
- nums[l] moves from index l to index r.
- Every element nums[i] for i in [l + 1, r] shifts left by 1 position to index i - 1.

Because each element in [l + 1, r] shifts left by 1 position, its position parity flips.
As a result, every element in nums[l + 1..r] flips its sign contribution in the total pulse sum.

The change in pulse value (Delta) simplifies based on the parity of l and r:
- Same Parity (l % 2 == r % 2):
    Delta = 2 * (P[l + 1] - P[r + 1])
- Different Parity (l % 2 != r % 2):
    Delta = 2 * (P[l] - P[r + 1])

Algorithm Approach:
1. Compute the base alternating sum base_pulse = P[n] and prefix sum array P of length n + 1.
2. Iterate through r from 1 to n - 1:
   - Maintain the maximum possible value of P[l + 1] and P[l] for l < r, split by parity of l:
     * max_Pl1_even: max P[l + 1] for even l < r
     * max_Pl1_odd:  max P[l + 1] for odd l < r
     * max_Pl_even:  max P[l] for even l < r
     * max_Pl_odd:   max P[l] for odd l < r
3. At index r:
   - If r is even:
     * Same parity (l is even): Delta = 2 * (max_Pl1_even - P[r + 1])
     * Different parity (l is odd): Delta = 2 * (max_Pl_odd - P[r + 1])
   - If r is odd:
     * Same parity (l is odd): Delta = 2 * (max_Pl1_odd - P[r + 1])
     * Different parity (l is even): Delta = 2 * (max_Pl_even - P[r + 1])
4. Return base_pulse + max(Delta, 0).


Complexity Analysis:
- Time Complexity: O(N) — Single pass to compute alternating prefix sums and a linear sweep to update max trackers and find max gain.
- Space Complexity: O(N) — Space for the alternating prefix sum array P.
"""
class Solution:
    def maxValue(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        P = [0] * (n + 1)
        for i in range(n):
            sign = 1 if i % 2 == 0 else -1
            P[i + 1] = P[i] + sign * nums[i]

        base_pulse = P[n]
        max_delta = 0

        INF = float('inf')
        max_Pl_even = -INF
        max_Pl_odd = -INF
        max_Pl1_even = -INF
        max_Pl1_odd = -INF

        for r in range(1, n):
            l = r - 1
            if l % 2 == 0:
                max_Pl_even = max(max_Pl_even, P[l])
                max_Pl1_even = max(max_Pl1_even, P[l + 1])
            else:
                max_Pl_odd = max(max_Pl_odd, P[l])
                max_Pl1_odd = max(max_Pl1_odd, P[l + 1])

            if r % 2 == 0:
                if max_Pl1_even != -INF:
                    max_delta = max(max_delta, 2 * (max_Pl1_even - P[r + 1]))
                if max_Pl_odd != -INF:
                    max_delta = max(max_delta, 2 * (max_Pl_odd - P[r + 1]))
            else:
                if max_Pl1_odd != -INF:
                    max_delta = max(max_delta, 2 * (max_Pl1_odd - P[r + 1]))
                if max_Pl_even != -INF:
                    max_delta = max(max_delta, 2 * (max_Pl_even - P[r + 1]))

        return base_pulse + max_delta
