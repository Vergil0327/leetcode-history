# We need a single DP state that tracks:

# Current Digit Sum: To check if the final sum is "Good."

# Monotone State: Are we currently strictly increasing, strictly decreasing, or already non-monotone?

# Previous Digit: To compare with the current digit.

# Key Components Explained:

# 1. Monotone Type Transition:

#     - Type 0: We have exactly one non-zero digit. The next digit will determine if we are increasing (1) or decreasing (2). If the next digit is the same, it's broken (3).

#     - Type 3: Once the digits are no longer strictly monotone, they can never become monotone again. However, we must keep tracking the current_sum because the number might still be "Fancy" if the final sum is Good.

# 2. The current_sum limit:

# With $10^{15}$, the maximum digit sum is $9 \times 15 = 135$. This is a very small state for the DP, making it efficient.

# 3. Inclusion-Exclusion via OR:

# By checking if (is_monotone or sum_is_good) at the very end of the digit string, we ensure that a number like 123 is only counted once, even if it satisfies both conditions.

# $$MaxSum = 9 \times 15 = 135$$We can create a list sum_is_good where sum_is_good[s] is True if $s$ is strictly monotone.
# precompute good_sums
good_sums = [False] * 151 # 9 * 15 + 1
for s in range(151):
    s_str = str(s)
    if len(s_str) == 1:
        good_sums[s] = True
    elif all(s_str[i] > s_str[i-1] for i in range(1, len(s_str))):
        good_sums[s] = True
    elif all(s_str[i] < s_str[i-1] for i in range(1, len(s_str))):
        good_sums[s] = True

    
def is_good(n):
    if n < 10: return True
    s = str(n)
    # Check increasing
    if all(s[i] > s[i-1] for i in range(1, len(s))): return True
    # Check decreasing
    if all(s[i] < s[i-1] for i in range(1, len(s))): return True
    return False

from functools import cache

class Solution:
    def countFancy(self, l: int, r: int) -> int:
        
        def solve(N_str):
            n = len(N_str)

            @cache
            def dp(i, is_less, is_started, prev_digit, monotone_type, current_sum):
                # monotone_type: 0: unknown, 1: strictly increasing, 2: strictly decreasing, 3: broken
                if i >= n:
                    # Fancy if (started and good) OR (started and digit sum is good)
                    is_monotone = is_started and monotone_type in [1, 2]
                    
                    # sum_is_good = is_started and is_good(current_sum)
                    # return 1 if (is_monotone or sum_is_good) else 0
                    
                    return 1 if (is_monotone or good_sums[current_sum]) else 0

                limit = int(N_str[i]) if not is_less else 9
                res = 0

                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            # Still haven't started
                            res += dp(i + 1, next_is_less, False, -1, 0, 0)
                        else:
                            # Starting the number with digit 'd'
                            # Every single-digit start is potentially inc or dec
                            # We'll treat a single digit as BOTH (type 1 and 2)
                            # To simplify, start as "type 0" and decide on second digit
                            res += dp(i + 1, next_is_less, True, d, 0, d)
                    else:
                        new_sum = current_sum + d
                        new_type = monotone_type
                        
                        if monotone_type == 0: # Second digit decision
                            if d > prev_digit: new_type = 1
                            elif d < prev_digit: new_type = 2
                            else: new_type = 3 # Equal digits break monotonicity
                        elif monotone_type == 1: # Must keep increasing
                            if d <= prev_digit: new_type = 3
                        elif monotone_type == 2: # Must keep decreasing
                            if d >= prev_digit: new_type = 3
                        
                        res += dp(i + 1, next_is_less, True, d, new_type, new_sum)
                
                return res

            return dp(0, False, False, -1, 0, 0)

        # Clear cache between calls to avoid interference
        ans_r = solve(str(r))
        ans_l = solve(str(l - 1))
        return ans_r - ans_l