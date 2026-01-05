"""
This problem can be solved row-by-row using Dynamic Programming.

The constraints $N, M, D \le 750$ suggest an $O(N \cdot M \cdot D)$ solution. A naive $O(N \cdot M^2)$ or $O(N \cdot M \cdot D^2)$ will be too slow.

DP State Definition

As hinted, we need to track if the last move was horizontal to enforce the "no two consecutive same-row moves" rule.

$dp0[r][c]$: Ways to reach cell $(r, c)$ where the last move was from row $r+1$ (moved UP).
$dp1[r][c]$: Ways to reach cell $(r, c)$ where the last move was within row $r$ (moved SAME-ROW).

Transitions

1. To get $dp0[r][c]$ (Moving from $r+1$ to $r$):You can come from any valid cell $(r+1, c_{prev})$ as long as the distance is $\le d$. Since the previous move to $r+1$ could have been either "Up" or "Same-row", we sum both:$$dp0[r][c] = \sum (dp0[r+1][c_{prev}] + dp1[r+1][c_{prev}]) \text{ where dist}((r,c), (r+1, c_{prev})) \le d$$
2. To get $dp1[r][c]$ (Moving within row $r$):You must have arrived at the previous cell $(r, c_{prev})$ via an UP move.$$dp1[r][c] = \sum (dp0[r][c_{prev}]) \text{ where dist}((r,c), (r, c_{prev})) \le d, c \neq c_{prev}$$

Optimization: Pre-calculating Row Windows

For a fixed row distance $\Delta r$, the condition $\sqrt{\Delta r^2 + \Delta c^2} \le d$ simplifies to:

$$|\Delta c| \le \sqrt{d^2 - \Delta r^2}$$

Let $W_{\Delta r} = \lfloor \sqrt{d^2 - \Delta r^2} \rfloor$. This means for a move from row $r_A$ to $r_B$, you only need to look at columns in the range $[c - W_{\Delta r}, c + W_{\Delta r}]$.
This allows us to use Prefix Sums to calculate the sum of DP values in a range in $O(1)$ time.

Implementation Plan

1. Initialize $dp0[n-1][c] = 1$ for all available cells in the bottom row. $dp1[n-1][c] = 0$.
2. For each row from $n-1$ down to $0$:
    - Same-row moves: Calculate $dp1[r][c]$ using prefix sums of $dp0[r]$. The window size is $W_0 = d$.
    - Up moves: Calculate $dp0[r-1][c]$ using prefix sums of $(dp0[r] + dp1[r])$. The window size is $W_1 = \sqrt{d^2 - 1}$.
"""

from math import isqrt


from typing import List

# TLE: O(N * M * M)
class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n = len(grid)
        m = len(grid[0])
        mod = 10**9 + 7
        
        # dp0[r][c] = ways to reach (r, c) via an UP move (from row r+1)
        # dp1[r][c] = ways to reach (r, c) via a SAME-ROW move (from row r)
        dp0 = [[0] * m for _ in range(n)]
        dp1 = [[0] * m for _ in range(n)]
        
        # INITIALIZATION: Starting at the bottom row (n-1)
        # We assume the "first" move to get onto the board is an "UP" move
        # so that we are allowed to immediately move horizontally if we want.
        for c in range(m):
            if grid[n-1][c] == '.':
                dp0[n-1][c] = 1

        # Process each row from bottom to top
        for r in range(n - 1, -1, -1):
            
            # --- STEP 1: SAME-ROW MOVES ---
            # "If you stay on the same row... your next move must go to the row above."
            # Therefore, a same-row move MUST come from a cell reached via an UP move.
            for c_to in range(m):
                if grid[r][c_to] == '#': continue
                
                for c_from in range(m):
                    if c_to == c_from: continue # Must be a different cell
                    if grid[r][c_from] == '#': continue
                    
                    # Euclidean distance on same row: sqrt((r-r)^2 + (c_to-c_from)^2)
                    dist_sq = (c_to - c_from)**2
                    if dist_sq <= d**2:
                        dp1[r][c_to] = (dp1[r][c_to] + dp0[r][c_from]) % mod

            # If we just finished row 0, we don't need to try moving "up" again
            if r == 0: break

            # --- STEP 2: UP MOVES ---
            # Move from row r to row r-1
            # You can move UP regardless of whether you reached row r via UP or SAME-ROW.
            for c_to in range(m):
                if grid[r-1][c_to] == '#': continue
                
                for c_from in range(m):
                    if grid[r][c_from] == '#': continue
                    
                    # Euclidean distance: sqrt(( (r-1)-r )^2 + (c_to-c_from)^2)
                    # vertical distance squared is always 1^2 = 1
                    dist_sq = 1 + (c_to - c_from)**2
                    if dist_sq <= d**2:
                        # Total ways at source is (Up-ways + Same-row-ways)
                        ways_at_source = (dp0[r][c_from] + dp1[r][c_from]) % mod
                        dp0[r-1][c_to] = (dp0[r-1][c_to] + ways_at_source) % mod

        # FINAL ANSWER: Total routes ending anywhere on the top row (row 0)
        total_routes = 0
        for c in range(m):
            total_routes = (total_routes + dp0[0][c] + dp1[0][c]) % mod
            
        return total_routes

# Optimized: O(N * M)
class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n, m = len(grid), len(grid[0])
        mod = 10**9 + 7
        
        # Precompute the maximum horizontal reach (W) for vertical distances 0 and 1
        # W = floor(sqrt(d^2 - delta_r^2))
        w0 = d # When delta_r = 0 (same row)
        w1 = isqrt(d**2 - 1) if d >= 1 else -1 # When delta_r = 1 (row above)
        
        # dp0[c]: reached via UP move. dp1[c]: reached via SAME-ROW move
        dp0 = [1 if grid[n-1][c] == '.' else 0 for c in range(m)]
        dp1 = [0] * m
        
        def get_sum(pref, left, right):
            left = max(0, left)
            right = min(m - 1, right)
            if left > right: return 0
            return (pref[right + 1] - pref[left]) % mod

        for r in range(n - 1, -1, -1):
            # 1. Handle SAME-ROW moves within current row 'r'
            # (only if we didn't just move up to reach row 0, though the problem says
            # the route ends at row 0, we can still move horizontally on row 0)
            pref0 = [0] * (m + 1)
            for i in range(m):
                pref0[i+1] = (pref0[i] + dp0[i]) % mod
            
            for c in range(m):
                if grid[r][c] == '.':
                    # sum of dp0 in range [c-w0, c+w0] excluding c itself
                    total = get_sum(pref0, c - w0, c + w0)
                    dp1[c] = (total - dp0[c]) % mod
                else:
                    dp1[c] = 0

            # If we are at the top row, we are done
            if r == 0: break
            
            # 2. Prepare for row r-1 (UP moves)
            next_dp0 = [0] * m
            # A move to r-1 can come from (dp0 + dp1) of row r
            combined_curr = [(dp0[i] + dp1[i]) % mod for i in range(m)]
            pref_combined = [0] * (m + 1)
            for i in range(m):
                pref_combined[i+1] = (pref_combined[i] + combined_curr[i]) % mod
            
            if w1 >= 0:
                for c in range(m):
                    if grid[r-1][c] == '.':
                        next_dp0[c] = get_sum(pref_combined, c - w1, c + w1)
            
            dp0 = next_dp0

        # The answer is the sum of all routes that ended at row 0
        return (sum(dp0) + sum(dp1)) % mod
