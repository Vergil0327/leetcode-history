"""
### Mathematical Property & Solution 1: Distinct Suffix ANDs

For any subarray nums[l..r], the bitwise AND of its elements is bounded above by 
every individual element in the subarray:
    AND(l, r) <= nums[k]   for all k in [l, r]
Thus, AND(l, r) <= min(l, r) always holds.

Equality AND(l, r) == min(l, r) holds if and only if the value x = AND(l, r) 
actually appears inside nums[l..r] (i.e., its most recent occurrence at or 
before index r satisfies last_pos[x] >= l).

---

### Algorithm (Range Compression of Suffix ANDs)

1. Monotonicity of Suffix ANDs:
   - Fix the right endpoint r and scan start index l from r down to 0.
   - As l moves left, the bitwise AND can only stay the same or clear at least 
     one set bit.
   - Because nums[i] <= 10^6 < 2^20, there are at most 21 distinct suffix AND 
     values at any right endpoint r.

2. Maintaining Ranges:
   - Maintain a compressed list of triples `[val, l_start, l_end]` partitioning 
     [0..r], representing that all starting indices l in [l_start, l_end] yield 
     AND(l, r) == val.
   - When advancing to r with element x = nums[r]:
     a. Record `last_pos[x] = r`.
     b. Update every existing range's value via `val &= x`.
     c. Append the new singleton range `[x, r, r]`.
     d. Merge adjacent ranges whose updated `val` has become equal.

3. Counting Valid Subarrays Ending at r:
   - For each compressed range `[val, l_start, l_end]`, we need starting indices 
     l in [l_start, l_end] such that `val` appears in nums[l..r].
   - This holds iff `l <= last_pos[val]`.
   - If `last_pos[val] >= l_start`, the number of valid starts in this range is:
         min(l_end, last_pos[val]) - l_start + 1

=== Solution 1 Complexity Analysis ===

1. Time Complexity: O(n * log(max(nums)))
   - At each index r, `ranges` contains at most log2(10^6) + 1 <= 21 intervals.
   - Updating, merging, and counting over `ranges` takes O(log(max(nums))) per step.
   - Total Time Complexity: O(n * log(max(nums))) ≈ 0.35s - 0.75s in Python for n = 2 * 10^5.

2. Space Complexity: O(n)
   - `last_pos` stores at most n distinct keys: O(n) auxiliary space.
   - `ranges` stores at most 21 triples: O(log(max(nums))).
"""
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        ans = 0
        last_pos = {}
        # Compressed list of [and_val, start_l, end_l] covering [0..r]
        ranges = []
        
        for r, x in enumerate(nums):
            last_pos[x] = r
            
            # Update existing suffix AND values with the new element x
            for item in ranges:
                item[0] &= x
            ranges.append([x, r, r])
            
            # Merge adjacent ranges that now share the same bitwise AND
            merged = []
            for item in ranges:
                if merged and merged[-1][0] == item[0]:
                    merged[-1][2] = item[2]
                else:
                    merged.append(item)
            ranges = merged
            
            # Count starting indices l where val appears inside nums[l..r]
            for val, l_start, l_end in ranges:
                pos = last_pos.get(val, -1)
                if pos >= l_start:
                    ans += min(l_end, pos) - l_start + 1
                    
        return ans