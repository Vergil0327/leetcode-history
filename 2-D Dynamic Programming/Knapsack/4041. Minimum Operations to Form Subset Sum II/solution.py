# Algorithm Approach:
# 1. Candidate Generation per Element:
#    - For a number x, divide it by 2 repeatedly: y = x // (2^d), incurring d division operations.
#    - For each resulting y, multiply it by 2 repeatedly: v = y * (2^m), incurring (d + m) total operations.
#    - Maintain a hash map 'candidates' storing the minimum operation cost to reach each unique value v <= sum.

# 2. Knapsack DP:
#    - Run standard 0/1 Knapsack DP using the generated candidates for each element.

# Complexity Analysis:
# - Time Complexity: O(N * S * log(max_val) * log(S)), where N = len(nums) <= 100 and S = target_sum <= 5000.
#   - Divisions loop runs at most log2(500) ≈ 9 times.
#   - Multiplications loop runs at most log2(5000) ≈ 13 times.
#   - Number of unique candidates per element is at most ~100.
#   - Total operations ≈ 100 * 5000 * 100 ≈ 5 * 10^7, which comfortably runs under 0.2s.
# - Space Complexity: O(S) for the DP table and candidate maps.
class Solution:
    def minOperations(self, nums: list[int], target_sum: int) -> int:
        dp = [float('inf')] * (target_sum + 1)
        dp[0] = 0
        
        for x in nums:
            # candidates[val] = min operations to form 'val' from x
            candidates = {}
            
            # Step 1: Perform d divisions
            d_ops = 0
            curr_div = x
            
            while True:
                # Step 2: Perform m multiplications on curr_div
                m_ops = 0
                val = curr_div
                
                while val <= target_sum:
                    cost = d_ops + m_ops
                    if val not in candidates or cost < candidates[val]:
                        candidates[val] = cost
                    
                    if val == 0:  # 0 * 2 is still 0, no need to double
                        break
                        
                    val *= 2
                    m_ops += 1
                
                if curr_div == 0:
                    break
                    
                curr_div //= 2
                d_ops += 1

            # 0/1 Knapsack DP transition
            next_dp = list(dp)
            for s in range(target_sum, -1, -1):
                if dp[s] == float('inf'):
                    continue
                for val, ops in candidates.items():
                    if val > 0 and s + val <= target_sum:
                        next_dp[s + val] = min(next_dp[s + val], dp[s] + ops)
            
            dp = next_dp
            
        return dp[target_sum] if dp[target_sum] != float('inf') else -1