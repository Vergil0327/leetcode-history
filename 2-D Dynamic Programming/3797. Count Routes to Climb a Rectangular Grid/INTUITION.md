This problem can be solved row-by-row using Dynamic Programming.

The constraints $N, M, D \le 750$ suggest an $O(N \cdot M \cdot D)$ solution. A naive $O(N \cdot M^2)$ or $O(N \cdot M \cdot D^2)$ will be too slow.

DP State Definition

As hinted, we need to track if the last move was horizontal to enforce the "no two consecutive same-row moves" rule.

$dp0[r][c]$: Ways to reach cell $(r, c)$ where the last move was from row $r+1$ (moved UP).

$dp1[r][c]$: Ways to reach cell $(r, c)$ where the last move was within row $r$ (moved SAME-ROW).

Transitions

1. To get $dp0[r][c]$ (Moving from $r+1$ to $r$): You can come from any valid cell $(r+1, c_{prev})$ as long as the distance is $\le d$. Since the previous move to $r+1$ could have been either "Up" or "Same-row", we sum both:
   
   $$dp0[r][c] = \sum (dp0[r+1][c_{prev}] + dp1[r+1][c_{prev}]) \text{ where dist}((r,c), (r+1, c_{prev})) \le d$$

2. To get $dp1[r][c]$ (Moving within row $r$):You must have arrived at the previous cell $(r, c_{prev})$ via an UP move.
   
   $$dp1[r][c] = \sum (dp0[r][c_{prev}]) \text{ where dist}((r,c), (r, c_{prev})) \le d, c \neq c_{prev}$$

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

