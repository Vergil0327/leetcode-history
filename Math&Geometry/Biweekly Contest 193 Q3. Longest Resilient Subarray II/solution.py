"""
### Mathematical Condition for Resilient Subarray

Let the subarray be nums[L...R] with total sum S = sum(nums[L...R]).
For every element x in nums[L...R]:
    (S - x) % k == 0  ==>  S % k == x % k

This implies two equivalent properties:
1. Every element in the resilient subarray must have the SAME remainder modulo k.
2. If the subarray length is M and each element has remainder r (where 0 <= r < k), then:
   S = M * r (mod k)
   Since S % k == r (mod k), we must have:
   M * r = r (mod k)  ==>  (M - 1) * r = 0 (mod k)

Therefore, a subarray nums[L...R] of length M is resilient if and only if:
1. All elements in nums[L...R] have the same remainder modulo k:
   nums[i] % k == r  for all i in [L, R]
2. (M - 1) * r % k == 0

### Algorithm Strategy

1. Split the array `nums` into contiguous segments where all elements share the exact same remainder modulo k.
2. For each segment of length L and remainder r:
   - If r == 0:
     (M - 1) * 0 % k == 0 is always TRUE for any length M >= 1.
     So the max length for this segment is L.
   - If r > 0:
     We need (M - 1) * r % k == 0, which means (M - 1) must be a multiple of k / gcd(r, k).
     Let step = k // gcd(r, k).
     We need (M - 1) to be a multiple of `step`, so valid M can be 1, 1 + step, 1 + 2*step, ...
     The largest valid M <= L is:
     M = 1 + ((L - 1) // step) * step.

3. Return the maximum valid length over all contiguous same-remainder segments.
"""
from math import gcd

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        
        i = 0
        while i < n:
            r = nums[i] % k
            j = i
            while j < n and nums[j] % k == r:
                j += 1
            
            # Segment nums[i...j-1] of length L has same remainder r
            L = j - i
            
            if r == 0:
                # Any length is valid for remainder 0
                max_len = L
            else:
                step = k // gcd(r, k)
                max_len = 1 + ((L - 1) // step) * step
                
            ans = max(ans, max_len)
            i = j
            
        return ans


# what if Constraints:
# 1 <= nums.length <= 2500
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
"""
### Algorithmic Strategy (Sliding Window / Two Pointers)

If we do not use the modular arithmetic property (M - 1) * r % k == 0 directly, we can evaluate resilience using its operational definition:

A subarray nums[L...R] with total sum S is resilient iff for every index i in [L, R]:
    (S - nums[i]) % k == 0

Notice that if we fix the left boundary L and expand the right boundary R:
1. The total sum S = sum(nums[L...R]) increases as R increases.
2. For every element nums[i] in the subarray, we check if (S - nums[i]) % k == 0.
3. If ANY element in nums[L...R] fails this condition, the subarray is NOT resilient.

Since N <= 2500, an O(N^2) dynamic checking approach or an optimized Sliding Window / Dynamic Programming approach works comfortably within time limits (2500^2 ≈ 6.25 * 10^6 operations).

"""

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        
        # Try every starting index L
        for l in range(n):
            current_sum = 0
            # Track remainder of the first element to ensure uniformity
            first_rem = nums[l] % k
            
            for r in range(l, n):
                # Optimization: All elements must have the same remainder mod k
                if nums[r] % k != first_rem:
                    break
                
                current_sum += nums[r]
                
                # Check resilience definition: (sum - element) % k == 0 for all elements
                # Since all elements have remainder `first_rem`, checking one element (or the first) is sufficient
                if (current_sum - nums[l]) % k == 0:
                    ans = max(ans, r - l + 1)
                    
        return ans

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        
        l = 0
        while l < n:
            r = l
            rem = nums[l] % k
            
            # Find max contiguous range with same remainder
            while r < n and nums[r] % k == rem:
                r += 1
            
            # For this block nums[l...r-1], check every candidate length length M
            block_len = r - l
            
            # Simulate window validation
            for M in range(1, block_len + 1):
                # Total sum modulo k for M elements with remainder `rem`
                sum_mod = (M * rem) % k
                # Removing one element leaves (sum_mod - rem) % k
                if (sum_mod - rem) % k == 0:
                    ans = max(ans, M)
                    
            l = r
            
        return ans