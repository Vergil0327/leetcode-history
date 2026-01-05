"""
see constraint:
    2 <= lists.length <= 12 => scale is small, even bitmask is suitable to store states

Think of DP with bitmask:


State Definition: Let dp(mask) be the minimum cost to merge the subset of lists represented by the bitmask into a single sorted list.

State Transition: To compute dp(mask), we split the mask into two non-empty sub-masks (sub1 and sub2) such that `sub1 Union sub2 = mask`.
  - The cost to get the final merged list for a mask is:dp(sub1) + dp(sub2) + {Cost to merge the resulting two lists}

Properties are fixed regardless of the order in which you merge a subset of lists, the resulting merged list will always have the same elements.
- Total Length: Sum of lengths of all lists in the mask.
- Median: The median of the combined, sorted elements of all lists in the mask.

Therefore, for every possible bitmask ($2^{12} = 4096$), we can precompute the total length and the median. To find the median efficiently, combine the sorted lists (using heapq.merge or simply sorting) once per mask.
"""


from typing import List
import functools

class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        
        # 1. Precompute length and median for every possible subset (mask)
        mask_info = {} # mask -> (length, median)
        getMedian = lambda arr: arr[(len(arr)-1) // 2]
        for bitmask in range(1, 1 << n):
            combined = []
            for i in range(n):
                if (bitmask >> i) & 1:
                    combined.extend(lists[i])
            
            combined.sort()
            mask_info[bitmask] = (len(combined), getMedian(combined))

        @functools.lru_cache(None)
        def dfs(state):
            # Base case: A single list has 0 cost to "merge" itself
            if bin(state).count('1') == 1:
                return 0
            
            res = float('inf')
            
            # Iterate through submasks to split the current mask into two groups
            # This is a standard trick to iterate over submasks:
            submask = (state - 1) & state
            while submask > 0:
                sub1 = submask
                sub2 = state ^ submask
                                
                l1, m1 = mask_info[sub1]
                l2, m2 = mask_info[sub2]
                
                # Cost = cost of internal merges + cost of this final merge
                current_merge_cost = l1 + l2 + abs(m1 - m2)
                total_cost = dfs(sub1) + dfs(sub2) + current_merge_cost
                
                res = min(res, total_cost)
                
                submask = (submask - 1) & state
            
            return res

        return dfs((1 << n) - 1)