"""
This simple solution works efficiently by exploiting a fundamental mathematical property of the Greatest Common Divisor (GCD) function on arrays.

Here is why this solution is both correct and fast enough to run in time:

Key Insight: Prefix GCDs Change Very Few Times
When computing prefix GCDs $g_i = \gcd(a_0, a_1, \dots, a_i)$, every time the GCD changes, it must become a proper divisor of the previous value. This means it must be divided by at least $2$.
Because numbers in nums are at most $10^9$, a prefix GCD can decrease at most $\approx 30$ times ($\log_2(10^9) \approx 30$) across the entire array!


"""

from math import gcd
from typing import List

class Solution:
    def solve(self, pre: List[int], suff: List[int], skip: int, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n + 1):
            if i - 1 == skip:
                pre[i] = pre[i - 1]
                continue
            pre[i] = gcd(pre[i - 1], arr[i - 1])
        for i in range(n - 1, -1, -1):
            if i == skip:
                suff[i] = suff[i + 1]
                continue
            suff[i] = gcd(suff[i + 1], arr[i])
        curr = 0
        for i in range(n - 1):
            if i == skip:
                continue
            if pre[i + 1] == suff[i + 1]:
                curr += 1
        return curr

    def maxValidSplits(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # 1. Precomputing Unmodified Prefix GCDs
        # premain[i] stores the prefix GCD of nums[0..i-1].
        premain = [0] * (n + 1)
        for i in range(1, n + 1):
            premain[i] = gcd(premain[i - 1], nums[i - 1])

        # 2. Skipping Equivalent Skip Indices (The Core Optimization)
        # This loop decides which index i - 1 to skip (remove).
        # If premain[i] == premain[i - 1], removing nums[i - 1] does not change the prefix GCD behavior up to i.
        # Because premain only changes at most $O(\log(\text{MAX\_VAL}))$ times, the continue statement skips almost all $N$ indices!
        # Thus, the loop only executes at most $\approx 30$ times instead of $N = 10^5$ times!
        for i in range(n + 1):
            if i > 0 and premain[i] == premain[i - 1]:
                continue

            # For the few critical candidate indices that do change the prefix GCD, solve() builds the prefix and suffix GCD arrays in $O(N)$ time, skipping the candidate index skip, and counts how many split positions satisfy pre[i + 1] == suff[i + 1].
            # Complexity Analysis
            # Total Candidates Checked: $O(\log(\text{MAX\_VAL})) \approx 30$.
            # Time Per Check (solve): $O(N \log(\text{MAX\_VAL}))$ for $N$ GCD computations.
            # Overall Time Complexity: $O(N \cdot \log^2(\text{MAX\_VAL})) \approx 30 \times 10^5 \times 30$ operations, which easily runs in $< 0.5$ seconds in Python!
            # Space Complexity: $O(N)$ for the auxiliary pre, suff, and premain arrays.
            pre = [0] * (n + 1)
            suff = [0] * (n + 1)
            ans = max(ans, self.solve(pre, suff, i - 1, nums))


        return ans