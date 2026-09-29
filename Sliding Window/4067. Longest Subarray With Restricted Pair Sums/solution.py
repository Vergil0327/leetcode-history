"""
================================================================================
KEY INSIGHT & APPROACH
================================================================================

1. Problem Reduction & Monotonicity:
   - A subarray is invalid if 3 distinct indices i, j, k satisfy nums[i] + nums[j] == nums[k].
   - If a subarray contains a violating triplet, any larger subarray containing it is 
     also invalid. This monotonicity allows using the Sliding Window (Two Pointers) technique.

2. Efficient Incremental Violation Counting:
   - Instead of checking all triplets in O(W^3) time per window, we maintain a `violations` 
     counter representing the total number of invalid triplets in the current window [l, r].
   - Since max(nums[i]) <= 500, we maintain a fixed-size frequency array `freq` of size 501.

3. State Updates:
   - When expanding right endpoint r (adding v = nums[r]):
     - As Sum (z = v): Count pairs (x, y) in window where x + y = v.
     - As Addend (x = v): Count pairs (y, z) in window where v + y = z.
   - When shrinking left endpoint l (removing u = nums[l]):
     - Decrement `freq[u]` first, then subtract the number of invalid triplets 
       formed by u with the remaining elements in [l+1, r].

4. Complexity:
   - Time Complexity: O(N * M), where N <= 1000 and M <= 500. Both pointers l and r 
     advance at most N times, running at most M operations per step (~10^6 ops max).
   - Space Complexity: O(M) for the fixed-size frequency array of size 501.
================================================================================
"""
class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        ans = 0
        freq = [0] * 501
        violations = 0
        
        for r in range(n):
            v = nums[r]
            
            # 1. Add violations where nums[r] acts as the sum z (v = x + y)
            for x in range(1, (v + 1) // 2):
                violations += freq[x] * freq[v - x]
            if v % 2 == 0:
                x = v // 2
                violations += freq[x] * (freq[x] - 1) // 2
                
            # 2. Add violations where nums[r] acts as an addend x (z = v + y)
            for y in range(1, 501 - v):
                violations += freq[y] * freq[v + y]
                
            freq[v] += 1
            
            # 3. Shrink window from the left while invalid
            while violations > 0:
                u = nums[l]
                freq[u] -= 1
                
                # Remove violations where nums[l] acted as the sum
                for x in range(1, (u + 1) // 2):
                    violations -= freq[x] * freq[u - x]
                if u % 2 == 0:
                    x = u // 2
                    violations -= freq[x] * (freq[x] - 1) // 2
                    
                # Remove violations where nums[l] acted as an addend
                for y in range(1, 501 - u):
                    violations -= freq[y] * freq[u + y]
                    
                l += 1
                
            ans = max(ans, r - l + 1)
            
        return ans