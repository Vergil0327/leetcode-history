# Algorithm Approach:
# 1. Reachable Values for a Single Element:
#    For any element x, because all multiplications must happen before divisions, a valid sequence of operations yields values formed by:
#    - Repeatedly doubling x: x, 2*x, 4*x, ... (cost = k multiplications)
#    - OR repeatedly floor-dividing x by 2: x, x//2, x//4, ... (cost = k divisions)
#    Any value obtained by multiplying and then dividing reduces to either pure multiplications or pure divisions (since multiplications canceled by divisions waste operations).
#    Thus, for each element nums[i], we can collect all reachable values v <= sum alongside the minimum operations required to achieve v.

# 2. Knapsack Dynamic Programming:
#    - Maintain a 1D DP array 'dp' of size (sum + 1) initialized to infinity (float('inf')), where dp[s] represents the minimum total operations to form subset sum s.
#    - Base case: dp[0] = 0.
#    - For each element x in nums:
#      - Generate all reachable values (v, cost) for x where v <= sum.
#      - Option A: Exclude element x from the subset (0 operations, adds 0 to sum).
#      - Option B: Replace x with value v using 'cost' operations, contributing v to the subset sum.
#      - Create a new DP array for the current step to ensure each element is used at most once:
#        new_dp[s] = min(dp[s], dp[s - v] + cost) for all reachable (v, cost).
#      - Update dp = new_dp.

# 3. Result:
#    - If dp[sum] is still infinity, return -1. Otherwise, return dp[sum].

# Complexity Analysis:
# - Time Complexity: O(N * S * log(S)), where N = len(nums) <= 100 and S = sum <= 5000. For each element, generating candidates takes O(log S) time, and updating the DP table takes O(S * log S). Total operations ≈ 100 * 5000 * 15 ≈ 7.5 * 10^6, easily passing within execution limits.
# - Space Complexity: O(S) to maintain the 1D DP table.

class Solution:
    def minOperations(self, nums: list[int], target_sum: int) -> int:
        # dp[s] = min operations to get subset sum 's'
        dp = [float('inf')] * (target_sum + 1)
        dp[0] = 0
        
        for x in nums:
            # Collect all (value, ops) achievable from x
            candidates = [(0, 0)]  # Option to not include this element in subset
            
            # 1. Pure divisions: x -> x//2 -> x//4 -> ...
            val, ops = x, 0
            while True:
                if val <= target_sum:
                    candidates.append((val, ops))
                if val == 0:
                    break
                val //= 2
                ops += 1
                
            # 2. Pure multiplications: x -> 2*x -> 4*x -> ...
            val, ops = x * 2, 1
            while val <= target_sum:
                candidates.append((val, ops))
                val *= 2
                ops += 1
            
            # 0/1 Knapsack transition using current element's reachable states
            next_dp = list(dp)
            for s in range(target_sum, -1, -1):
                if dp[s] == float('inf'):
                    continue
                for val, ops in candidates:
                    if val > 0 and s + val <= target_sum:
                        next_dp[s + val] = min(next_dp[s + val], dp[s] + ops)
            
            dp = next_dp
            
        return dp[target_sum] if dp[target_sum] != float('inf') else -1
