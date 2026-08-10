"""
1. Monotonicity for Binary Search
If two non-overlapping $k \times k$ squares consisting entirely of 1s exist, then taking a $(k-1) \times (k-1)$ sub-square inside each of them also yields two non-overlapping $(k-1) \times (k-1)$ squares. Thus, the existence of valid $k \times k$ squares is monotonic with respect to $k$, allowing us to binary search for $k \in [1, \min(m, n)]$.

2. Fast Square Checking with 2D Prefix Sums
We can build a 2D prefix sum array $P$ in $O(m \times n)$ time. A $k \times k$ square starting at top-left corner $(r, c)$ consists entirely of 1s if and only if its sum equals $k^2$, which can be queried in $O(1)$ time.

3. Checking Non-Overlap in $O(1)$ Space
For a fixed side length $k$, let $(r, c)$ be the top-left corner of a valid $k \times k$ square of 1s:

- Two squares with top-left corners $(r_1, c_1)$ and $(r_2, c_2)$ are non-overlapping if and only if:
    $$\vert{}r_1 - r_2\vert{} \ge k \quad \text{OR} \quad \vert{}c_1 - c_2\vert{} \ge k$$
- To check if any pair of valid top-left corners satisfies this condition, we only need to track the minimum and maximum row indices ($r_{\min}, r_{\max}$) and column indices ($c_{\min}, c_{\max}$) among all valid top-left corners:
    $$\text{Two valid squares exist} \iff (r_{\max} - r_{\min} \ge k) \quad \text{OR} \quad (c_{\max} - c_{\min} \ge k)$$
"""
class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # 1. Build 2D Prefix Sum
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                P[r + 1][c + 1] = mat[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]
                
        def can_fit(k: int) -> bool:
            r_min, r_max = float('inf'), float('-inf')
            c_min, c_max = float('inf'), float('-inf')
            count = 0
            target_sum = k * k
            
            # Check all possible top-left corners for a k x k square
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    # Query sum of k x k square with top-left (r, c)
                    sq_sum = P[r + k][c + k] - P[r][c + k] - P[r + k][c] + P[r][c]
                    
                    if sq_sum == target_sum:
                        count += 1
                        r_min = min(r_min, r)
                        r_max = max(r_max, r)
                        c_min = min(c_min, c)
                        c_max = max(c_max, c)
                        
            # Need at least two valid squares
            if count < 2:
                return False
                
            # Disjoint in rows or disjoint in columns
            return (r_max - r_min >= k) or (c_max - c_min >= k)

        # 2. Binary Search for maximum side length k
        low, high = 1, min(m, n)
        best_k = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_fit(mid):
                best_k = mid
                low = mid + 1  # Try larger side length
            else:
                high = mid - 1 # Try smaller side length
                
        return best_k * best_k