"""
### Problem Breakdown & Core Idea

We are asked to count the number of triplets (i, j, k) with 0 <= i <= j < k < n such that:
    distinct(s[i..j]) == distinct(s[j + 1..k])

Notice that any valid pair of substrings (s1, s2) is separated by a split point between index j and j + 1:
- s1 ends at j (starting at some i <= j).
- s2 starts at j + 1 (ending at some k >= j + 1).

If for a fixed split point j, we know:
- L[d]: number of starting indices i <= j such that distinct(s[i..j]) == d
- R[j + 1][d]: number of ending indices k >= j + 1 such that distinct(s[j + 1..k]) == d

Then the number of valid triplets for this split point j is simply:
    Sum_{d=1}^{26} (L[d] * R[j + 1][d])

---

### Key Optimization: Distinct Count as Intervals (O(N * 26))

Instead of iterating over every possible (i, j) and (j + 1, k) which would take O(N^2) time:

1. Right Substrings s[start..k]:
   - For a fixed `start`, as k moves right from `start` to `n - 1`, the number of distinct characters is non-decreasing and can only increase at most 26 times.
   - Specifically, the distinct count increases by 1 only at the FIRST occurrence of each distinct character at or after `start`.
   - If we collect the first occurrences of all characters that appear in `s[start..n-1]` and sort them in ascending order:
         start = p_0 < p_1 < p_2 < ... < p_{m-1} <= n - 1  (m <= 26)
   - Then:
     - For all k in [p_0, p_1 - 1], distinct count is 1. There are (p_1 - p_0) such endpoints k.
     - For all k in [p_1, p_2 - 1], distinct count is 2. There are (p_2 - p_1) such endpoints k.
     - ...
     - For all k in [p_{m-1}, n - 1], distinct count is m. There are (n - p_{m-1}) such endpoints k.

2. Left Substrings s[i..j]:
   - By the same logic, looking backwards from j to 0, the distinct count increases by 1 only at the MOST RECENT occurrence of each character before or at j.
   - Sorting these positions in descending order gives the counts of i for each distinct value d in O(26 log 26) time.

This reduces the complexity from O(N^2) to O(N * |Σ| log |Σ|) where |Σ| <= 26, running in under 0.08s for N = 2000.

=== Complexity Analysis ===

1. Time Complexity:
   - For each start index (n steps), we sort at most 26 elements: O(n * |Σ| log |Σ|)
   - For each split index j (n steps), we sort at most 26 elements: O(n * |Σ| log |Σ|)
   - Here |Σ| = 26 (lowercase English letters).
   - Total operations: ~2000 * 26 * log2(26) ≈ 2.5 * 10^5 operations, executing in ~0.07 seconds.

2. Space Complexity:
   - Table R of size n x 27: O(n * |Σ|) ≈ 2000 x 27 integers (~216 KB).
   - Tracking arrays next_pos and prev_pos of size 26: O(|Σ|).
   - Total auxiliary space: O(n * |Σ|).
"""

class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        s_int = [ord(c) - 97 for c in s]
        
        # R[start][d] = number of k >= start such that distinct(s[start..k]) == d
        R = [[0] * 27 for _ in range(n)]
        
        # Precompute R from right to left
        next_pos = [-1] * 26
        for start in range(n - 1, 0, -1):
            next_pos[s_int[start]] = start
            
            # Sorted first occurrence positions of characters appearing at or after start
            positions = sorted(p for p in next_pos if p != -1)
            row = R[start]
            
            for d in range(len(positions)):
                nxt = positions[d + 1] if d + 1 < len(positions) else n
                row[d + 1] = nxt - positions[d]

        # Scan left substrings for each split point j
        ans = 0
        prev_pos = [-1] * 26
        
        for j in range(n - 1):
            prev_pos[s_int[j]] = j
            
            # Sorted most recent occurrence positions looking backwards from j
            positions = sorted((p for p in prev_pos if p != -1), reverse=True)
            row_R = R[j + 1]
            
            for d in range(len(positions)):
                nxt = positions[d + 1] if d + 1 < len(positions) else -1
                count_L = positions[d] - nxt
                
                # Match s1 with s2 having distinct character count equal to d + 1
                if row_R[d + 1]:
                    ans += count_L * row_R[d + 1]
                    
        return ans
