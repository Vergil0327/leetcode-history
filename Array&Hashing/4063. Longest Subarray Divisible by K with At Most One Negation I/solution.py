# Mathematical Insight & Decomposition:

# 1. Modulo Arithmetic on Subarray Sums:
#    A subarray nums[i..j] has sum S(i, j) = P[j + 1] - P[i], where P is the prefix sum array.
#    The condition that S(i, j) is divisible by k without negation is:
#      (P[j + 1] - P[i]) % k == 0  ==>  P[j + 1] % k == P[i] % k

# 2. Effect of Negating One Element nums[m] (where i <= m <= j):
#    When nums[m] is negated to -nums[m], the new sum becomes:
#      S_new = S(i, j) - 2 * nums[m]
   
#    We want S_new % k == 0, which means:
#      (P[j + 1] - P[i] - 2 * nums[m]) % k == 0
#    Rearranging for P[i]:
#      P[i] % k == (P[j + 1] - 2 * nums[m]) % k

# 3. Small Constraints Optimization (N <= 1000):
#    Since N <= 1000, an O(N^2) or O(N^2) with small constant factor approach easily passes within time limits (N^2 = 10^6 operations).

#    For each starting index i (0 <= i < N):
#      - Maintain the current running sum S = 0.
#      - Also track the set or map of remainder values produced by (2 * nums[m]) % k for all m in range [i..j].
#      - For each ending index j (i <= j < N):
#        1. Update running sum: S = (S + nums[j]) % k.
#        2. Check Case 1 (No negation):
#           If S == 0, then nums[i..j] is valid without negation. Maximize max_len with (j - i + 1).
#        3. Check Case 2 (With one negation):
#           We need (S - 2 * nums[m]) % k == 0 for some m in [i..j], which is equivalent to:
#           (2 * nums[m]) % k == S % k.
#           If S % k exists in our tracked (2 * nums[m]) % k values for range [i..j], then nums[i..j] is valid with one negation.
#           Maximize max_len with (j - i + 1).

# Algorithm Approach (O(N^2)):
# 1. Initialize max_len = 0.
# 2. For each i from 0 to N - 1:
#    - Initialize running_sum = 0.
#    - Initialize a set or boolean array `seen_mods` to track (2 * nums[m]) % k values seen in range [i..j].
#    - For each j from i to N - 1:
#      * running_sum = (running_sum + nums[j]) % k
#      * Add (2 * nums[j]) % k (handling negative modulo correctly) to `seen_mods`.
#      * If running_sum == 0 or (running_sum in seen_mods):
#          max_len = max(max_len, j - i + 1)
# 3. Return max_len.

# Complexity Analysis:
# - Time Complexity: O(N^2) — Outer loop runs N times, inner loop runs up to N times with O(1) average hash set insertions and lookups. Total time < 0.05 seconds for N = 1000.
# - Space Complexity: O(N) — Space for `seen_mods` hash set storing at most N unique remainders per outer iteration.

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            running_sum = 0
            seen_mods = set()

            for j in range(i, n):
                running_sum = (running_sum + nums[j]) % k
                
                # Modulo 2 * nums[j]
                mod_2x = (2 * nums[j]) % k
                seen_mods.add(mod_2x)

                # Check if sum is divisible directly OR if negating some element makes it divisible
                if running_sum == 0 or running_sum in seen_mods:
                    max_len = max(max_len, j - i + 1)

        return max_len