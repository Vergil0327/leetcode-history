# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
be honestly, the first thought I have is using BFS with priority queue.
then, I realize even I always choose minimum value to fall, it can't guarantee that I can always get the minimum falling path.
because path is not **only**, I need to try all the path and choose minimum one.
now, I finally know this is a DP problem, and the recursive eq. is clear.

#### definition of `dp[r][c]`:
        
        the minimum falling path to reach matrix[r][c]

#### state transfer fn:

since we can fall from previous row's `col-1`, `col` and `col+1` to `current row and col`

        dp[r][c] = min(matrix[r-1][c-1] + dp[r-1][c-1], matrix[r-1][c-1]+dp[r-1][c], matrix[r-1][c-1]+dp[r-1][c+1])

#### base case

        1. set default value to `inf` since we need to find minimum
        2. append extra row & column to prevent out-of-bound error
        3. the minimum falling sum to 0-th row is 0 -> dp[0][col] = 0

once we got all these information,
we update our dp and choose minimum from `dp[last row]`

# Space Optimized

since our dp only depend on previous row, we only need to keep tracks of current and previous `dp` state.

we can optimize our space complexity from 2-D array to 1-D array

it's easy to optimize space complexity and get `dp[i]` once we know the original `dp[i][j]`

# Top-Down + Memorization

if we don't care space, top-down DP is more straight-forward.
just simulate falling

# Complexity
- Time complexity:
O($n^2$)

- Space complexity:

    $$O(n*n)$$ or $$O(n)$$

# Code
```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf] * (n+2) for _ in range(n+2)]
        for i in range(n+1):
            dp[0][i] = 0
        
        for r in range(1, n+1):
            for c in range(1, n+1):
                dp[r][c] = min(matrix[r-1][c-1] + dp[r-1][c-1], matrix[r-1][c-1]+dp[r-1][c], matrix[r-1][c-1]+dp[r-1][c+1])

        return min(dp[n])
```

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = [inf] * (n+2)
        curr = [inf] * (n+2)

        # base case
        for i in range(1, n+1):
            prev[i] = 0
        
        for r in range(1, n+1):
            for c in range(1, n+1):
                # dp[r][c] = min(matrix[r-1][c-1] + dp[r-1][c-1], matrix[r-1][c-1]+dp[r-1][c], matrix[r-1][c-1]+dp[r-1][c+1])
                curr[c] = min(matrix[r-1][c-1]+prev[c-1], matrix[r-1][c-1]+prev[c], matrix[r-1][c-1]+prev[c+1])
            prev, curr = curr, prev

        return min(prev)
```