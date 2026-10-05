"""
### Comparison: Single-Pass State DP vs. Prefix-Suffix DP

#### 1. Space & Memory Overhead
- Single-Pass DP:
  - Space Complexity: O(1)
  - Aux memory: 4 state variables (`dp0_no_del`, `dp1_no_del`, `dp0_del`, `dp1_del`).
  - Cache performance: Excellent (sequential array access, tiny memory footprint).

- Prefix-Suffix DP:
  - Space Complexity: O(N)
  - Aux memory: Four arrays of length N (`L_odd`, `L_even`, `R_pos`, `R_neg`).
  - Cache performance: Requires 3 total passes over array data (left-to-right, right-to-left, combine pass).

#### 2. Code Complexity & Maintainability
- Single-Pass DP:
  - Shorter code, but state transitions are dense and require careful reasoning around parity tracking and deletion states.
  - Less room for out-of-bounds indexing errors since updates happen element-by-element inline.

- Prefix-Suffix DP:
  - More explicit and modular structure (build prefix states, build suffix states, iterate deletion index `i`).
  - Easier to debug individually by inspecting precomputed arrays.

#### 3. Edge Cases & Boundary Handling
Both solutions handle the core constraints correctly:
- Array length = 1:
  - Single-Pass DP: Output is `nums[0]` (no deletion chosen).
  - Prefix-Suffix DP: Left and right bounds naturally evaluate to `-INF`, correctly falling back to max single-element score.
- Deleting boundary elements (index 0 or index N-1):
  - Single-Pass DP: Handled implicitly as elements transition through deletion states.
  - Prefix-Suffix DP: Handled by setting `left_odd`/`left_even` or `right_pos`/`right_neg` to `-INF` when index `i` is at 0 or N-1.
- All-negative input arrays:
  - Both approaches properly track single-element candidates (e.g. `max(x, ...)`) to ensure negative elements can form non-empty single-element subarrays rather than returning 0 or invalid combinations.
"""
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        INF = float('inf')
        
        # States initialized to -infinity
        dp0_no_del = -INF  # Even length, 0 deletions
        dp1_no_del = -INF  # Odd length, 0 deletions
        dp0_del = -INF     # Even length, 1 deletion
        dp1_del = -INF     # Odd length, 1 deletion
        
        ans = -INF
        
        for x in nums:
            # New state calculations
            
            # Odd length (starts with +x)
            new_dp1_no_del = max(x, dp0_no_del + x)
            new_dp1_del = max(dp1_no_del, dp0_del + x if dp0_del != -INF else -INF)
            
            # Even length (appends -x)
            new_dp0_no_del = dp1_no_del - x if dp1_no_del != -INF else -INF
            new_dp0_del = max(dp0_no_del, dp1_del - x if dp1_del != -INF else -INF)
            
            # Update states
            dp1_no_del, dp0_no_del = new_dp1_no_del, new_dp0_no_del
            dp1_del, dp0_del = new_dp1_del, new_dp0_del
            
            # The maximum alternating sum can end at any odd or even state
            ans = max(ans, dp1_no_del, dp0_no_del, dp1_del, dp0_del)
            
        return ans

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        INF = float('inf')
        
        # L_odd[i]: max alternating sum ending at i with odd length
        # L_even[i]: max alternating sum ending at i with even length
        L_odd = [-INF] * n
        L_even = [-INF] * n
        
        for i in range(n):
            x = nums[i]
            L_odd[i] = max(x, (L_even[i - 1] + x) if i > 0 else -INF)
            L_even[i] = (L_odd[i - 1] - x) if i > 0 else -INF
            
        # R_pos[i]: max alternating sum starting at i with '+' sign on nums[i]
        # R_neg[i]: max alternating sum starting at i with '-' sign on nums[i]
        R_pos = [-INF] * n
        R_neg = [-INF] * n
        
        for i in range(n - 1, -1, -1):
            x = nums[i]
            R_pos[i] = max(x, x + (R_neg[i + 1] if i + 1 < n else 0))
            R_neg[i] = -x + max(0, (R_pos[i + 1] if i + 1 < n else 0))

        # Overall maximum without any deletions
        ans = max(max(L_odd), max(L_even))
        
        # Try deleting each element nums[i]
        for i in range(n):
            left_odd = L_odd[i - 1] if i > 0 else -INF
            left_even = L_even[i - 1] if i > 0 else -INF
            
            right_pos = R_pos[i + 1] if i + 1 < n else -INF
            right_neg = R_neg[i + 1] if i + 1 < n else -INF
            
            # Case 1: Delete nums[i], combine left and right segments
            if left_odd != -INF and right_neg != -INF:
                ans = max(ans, left_odd + right_neg)
            if left_even != -INF and right_pos != -INF:
                ans = max(ans, left_even + right_pos)
                
            # Case 2: Subarray starts strictly after index i (only right segment)
            if right_pos != -INF:
                ans = max(ans, right_pos)
                
            # Case 3: Subarray ends strictly before index i (only left segment)
            if left_odd != -INF:
                ans = max(ans, left_odd)
            if left_even != -INF:
                ans = max(ans, left_even)

        return ans