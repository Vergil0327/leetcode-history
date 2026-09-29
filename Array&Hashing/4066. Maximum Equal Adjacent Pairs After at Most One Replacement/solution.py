from collections import Counter

"""
================================================================================
KEY INSIGHT & APPROACH
================================================================================

1. Effect of Replacing x with y (x != y):
   - Existing equal pairs (u == v):
     - If u == v == x, both become y (y == y). Still equal.
     - If u == v != x, neither changes value. Still equal.
     - All pre-existing equal pairs remain equal regardless of replacement.

   - Unequal pairs (u != v):
     - A pair becomes equal IF AND ONLY IF its elements are {x, y} (i.e., one 
       element is x and the other is y). Replacing x with y makes both equal to y.
     - Any pair containing only one of {x, y} and another value z (where z != x, y)
       becomes (y, z), which remains unequal because y != z.

2. Problem Reduction:
   - The final count of equal adjacent pairs for a chosen replacement pair (x, y) is:
       Total Equal Pairs = Base Equal Pairs + Count of adjacent pairs {x, y}
   - To maximize the final count, we simply need to find the most frequent 
     unordered pair of adjacent distinct elements in `nums`.

3. Complexity:
   - Time Complexity: O(N) — single pass to count adjacent pairs and aggregate counts.
   - Space Complexity: O(N) — to store counts of unique adjacent pairs in a hash map.
================================================================================
"""
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base_equal = 0
        pair_counts = Counter()
        
        for i in range(len(nums) - 1):
            u, v = nums[i], nums[i + 1]
            if u == v:
                base_equal += 1
            else:
                # Store unordered pair of adjacent distinct elements
                pair = (u, v) if u < v else (v, u)
                pair_counts[pair] += 1
                
        # Maximum additional equal pairs achievable by replacing x with y
        max_pair_gain = max(pair_counts.values()) if pair_counts else 0
        
        return base_equal + max_pair_gain