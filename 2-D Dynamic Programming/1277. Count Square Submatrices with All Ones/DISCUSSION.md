##### Top-Down with Memorization

intuition:
explore every cell if we can enlarge our square. 
use post-ordr DFS to count squares

analysis:
since we only caluculate once at each cell, the time complexity is `O(mn)`
space complexity is size of memorization, `O(mn)`

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        memo = {}
        def dfs(r, c):
            if r == m or c == n: return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            if matrix[r][c] == 1:
                memo[(r,c)] = 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))
            else:
                memo[(r,c)] = 0
            return memo[(r,c)]
        
        cnt = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]:
                    cnt += dfs(row, col)

        return cnt
```

##### Bottom-Up

intuition:

definition: `dp[i][j]: side length of largest square submatrices`

if we know that dp[i][j] equals to 2, that means we can found two squares at (i, j) position:

1. one is square with side which equals to 1
2. the other is square with side which equals to 2

so sum(dp) is our answer

time: O(mn)
space: O(mn)
```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = matrix[i-1][j-1]

		total = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
					total += dp[i][j]

        # return sum(map(sum, dp))
		return total
```

##### Space-Optimized Bottom-Up

once we got our bottom-up solution, it's easy to reduce our `space complexity` to `O(n)` since our dp only depends on previous state

time: O(mn)
space: O(n)

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp, prevDp = [0]*(n+1), [0]*(n+1)

        total = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = matrix[i-1][j-1] # initialization

                if matrix[i-1][j-1] == 1:
                    dp[j] = 1 + min(prevDp[j-1], prevDp[j], dp[j-1])
                    total += dp[j]
            dp, prevDp = prevDp, dp

        return total
```