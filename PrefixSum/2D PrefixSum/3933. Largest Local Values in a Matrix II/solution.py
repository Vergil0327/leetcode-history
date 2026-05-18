"""
The constraints on the matrix size are $n, m \le 200$, and the cell values are also bounded by $0 \le \text{matrix}[r][c] \le 200$.
A naive brute-force approach that scans the neighborhood for every cell would take $O(n \cdot m \cdot x^2)$ time. 
In the worst-case scenario where $x = 200$, this results in around $200^4 = 1.6 \times 10^9$ operations, which will cause a TLE (Time Limit Exceeded).

The Strategy: 2D Prefix Sums by Threshold

Since the maximum possible value in the matrix is small ($\le 200$), we can optimize the queries using 2D Prefix Sums
For a cell $(r, c)$ with value $x$, it is a local maximum if and only if there are zero cells in its considered neighborhood with a value strictly greater than $x$.
Instead of scanning the neighborhood, we can count how many cells in the bounding box have a value $> x$ in $O(1)$ time.
We do this by precomputing a 2D prefix sum array for each possible value $v \in [0, 200]$.

Bounding Box and Ignored Corners

For a cell $(r, c)$ with value $x$:

1. The rows considered are bounded by $[r - x, r + x]$.
2. The columns considered are bounded by $[c - x, c + x]$.
3. The Corners: We must ignore the four specific cells where both the row and column distances are exactly $x$:

    - $(r - x, c - x)$
    - $(r - x, c + x)$
    - $(r + x, c - x)$
    - $(r + x, c + x)$

Our prefix sum for a threshold $x$ will give us the total count of elements $> x$ inside the full $(2x+1) \times (2x+1)$ bounding box.
If any of the 4 corner cells contain a value $> x$, they will have been included in this prefix sum count.
Since the problem explicitly tells us to ignore these corners, we must check them individually and subtract them from our count if they are valid and strictly greater than $x$.
"""
from typing import List

class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        MAX_VAL = 200
        
        # prefix_sums[v][r][c] will store the number of cells in matrix[0...r-1][0...c-1] 
        # that have a value strictly greater than v.
        prefix_sums = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(MAX_VAL + 1)]
        
        # 1. Precompute the 2D prefix sums for each threshold value v
        for v in range(MAX_VAL + 1):
            for r in range(n):
                for c in range(m):
                    is_greater = 1 if matrix[r][c] > v else 0
                    prefix_sums[v][r + 1][c + 1] = (
                        is_greater 
                        + prefix_sums[v][r][c + 1] 
                        + prefix_sums[v][r + 1][c] 
                        - prefix_sums[v][r][c]
                    )
                    
        def query_rectangle(v, r1, c1, r2, c2):
            """Returns the count of cells > v in the bounding box [r1..r2] and [c1..c2]"""
            # Clamp boundaries to remain inside the matrix
            r1 = max(0, r1)
            c1 = max(0, c1)
            r2 = min(n - 1, r2)
            c2 = min(m - 1, c2)
            
            if r1 > r2 or c1 > c2:
                return 0
                
            return (
                prefix_sums[v][r2 + 1][c2 + 1]
                - prefix_sums[v][r1][c2 + 1]
                - prefix_sums[v][r2 + 1][c1]
                + prefix_sums[v][r1][c1]
            )

        ans = 0
        
        # 2. Check each cell to see if it is a local maximum
        for r in range(n):
            for c in range(m):
                x = matrix[r][c]
                if x == 0: continue # Local maximums must be non-zero
                
                # Get total count of cells > x in the full subgrid window
                count = query_rectangle(x, r - x, c - x, r + x, c + x)
                
                # Handle the 4 ignored corner cells
                corners = [
                    (r - x, c - x),
                    (r - x, c + x),
                    (r + x, c - x),
                    (r + x, c + x)
                ]
                
                for cr, cc in corners:
                    if 0 <= cr < n and 0 <= cc < m:
                        if matrix[cr][cc] > x:
                            count -= 1
                            
                # If no valid, considered neighbor is greater than x, it's a local maximum
                if count == 0:
                    ans += 1
                    
        return ans