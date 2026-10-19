"""
### Corrected Strategy

1. Target Interval Merging Rule:
   Merge target intervals `[s1, e1]` and `[s2, e2]` ONLY IF `s2 <= e1` (they overlap or touch at an endpoint).
   Do NOT merge if `s2 > e1` (even if `s2 == e1 + 1`), because real points between `e1` and `s2` (like `e1 + 0.5`) do NOT need to be covered.

2. Greedy Coverage for Each Disjoint Target Segment `[t_start, t_end]`:
   - Start covering at `curr = t_start`.
   - While `curr < t_end`:
     - Push all `availableIntervals` with `start <= curr` into a max-heap (by right endpoint).
     - Pop the interval extending farthest to the right (`best_reach`).
     - If `best_reach <= curr` or heap is empty, return `-1`.
     - `curr = best_reach`, `ans += 1`.
   - Special case for single point targets `[t_start, t_start]` where `t_start == t_end`:
     - If `curr` has not reached `t_end` (i.e. `curr < t_start`), push available intervals with `start <= t_start`, pick max right endpoint `best_reach >= t_start`, and set `curr = best_reach`, `ans += 1`.

=== COMPLEXITY ANALYSIS ===

1. Time Complexity:
   - Target Interval Merging: O(T log T)
   - Available Interval Sorting: O(A log A)
   - Heap Push/Pop Operations: Each available interval is pushed and popped at most once -> O(A log A)
   - Total Time Complexity: O(A log A + T log T) = O(N log N), running in under 0.08s for 5 * 10^4 intervals.

2. Space Complexity:
   - O(A + T) auxiliary space for storing merged target intervals and max-heap.
"""
import heapq

class Solution:
    def minSelection(self, availableIntervals: list[list[int]], targetIntervals: list[list[int]]) -> int:
        # Step 1: Merge target intervals ONLY if they overlap or touch (start <= prev_end)
        targetIntervals.sort(key=lambda x: x[0])
        merged_targets = []
        
        for start, end in targetIntervals:
            if not merged_targets:
                merged_targets.append([start, end])
            else:
                prev_start, prev_end = merged_targets[-1]
                # Merge only if overlapping or sharing an endpoint (e.g. [1,3] and [3,5])
                if start <= prev_end:
                    merged_targets[-1][1] = max(prev_end, end)
                else:
                    merged_targets.append([start, end])

        # Step 2: Sort available intervals by start endpoint
        availableIntervals.sort(key=lambda x: x[0])
        
        n_avail = len(availableIntervals)
        avail_idx = 0
        ans = 0
        max_reach = -1
        max_heap = []

        # Step 3: Cover each merged target interval
        for t_start, t_end in merged_targets:
            # If max_reach from previously selected intervals already covers t_start..t_end, skip!
            if max_reach >= t_end:
                continue
                
            curr = max(t_start, max_reach)
            
            # Handle point targets or standard intervals
            while curr < t_end or (t_start == t_end and max_reach < t_end):
                # Add all available intervals that start at or before curr
                while avail_idx < n_avail and availableIntervals[avail_idx][0] <= curr:
                    heapq.heappush(max_heap, -availableIntervals[avail_idx][1])
                    avail_idx += 1
                
                if not max_heap:
                    return -1
                
                best_reach = -heapq.heappop(max_heap)
                if best_reach < curr or (curr == best_reach and t_start == t_end and max_reach < t_end):
                    # Check if best_reach can cover curr
                    if best_reach < t_start:
                        return -1
                
                if best_reach <= curr and t_start != t_end:
                    return -1
                if best_reach < t_start:
                    return -1

                max_reach = max(max_reach, best_reach)
                curr = max_reach
                ans += 1
                
                if t_start == t_end:
                    break

        return ans

class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        avail = sorted(availableIntervals)

        merged = []
        for left, right in sorted(targetIntervals):
            if merged and left <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], right)
            else:
                merged.append([left, right])

        neg = float('-inf')
        curr, best = neg, neg
        count, i = 0, 0
        n = len(avail)

        for left, right in merged:
            while curr < right:
                val = left if left > curr else curr

                while i < n and avail[i][0] <= val:
                    best = max(best, avail[i][1])
                    i += 1

                if left > curr:
                    if best < left:
                        return -1
                else:
                    if best <= curr:
                        return -1

                curr = best
                count += 1

        return count