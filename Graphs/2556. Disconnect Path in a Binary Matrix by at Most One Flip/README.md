[2556. Disconnect Path in a Binary Matrix by at Most One Flip](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/description/)

`Medium`

You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

```
Example 1:
Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.

Example 2:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).
```

Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 10^5
- grid[i][j] is either 0 or 1.
- grid[0][0] == grid[m - 1][n - 1] == 1

<details>
<summary>Hint 1</summary>

We can consider the grid a graph with edges between adjacent cells.

</details>

<details>
<summary>Hint 2</summary>

If you can find two non-intersecting paths from (0, 0) to (m - 1, n - 1) then the answer is false. Otherwise, it is always true.

</details>

<details>
<summary>Solution</summary>

[Lee215 - Count Points on Diagonal](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/solutions/3141701/python-count-points-on-diagonal/?orderBy=most_votes)

Keep A[i][j] == 1 for points that
on the cnnected path from (0,0) to (m-1, n-1),
assigne all other A[i][j] = 0,
since we won't use them in the path.

If we can't disconnect (0,0) and (m-1, n-1),
this means we can always have 2 candidates,
we don't have to pass a specific point.

Notice all points on the diagonal from top-right to bottom-left,
have same distance from (0,0),
have same distance from (0,0).

So we count the point on each diagonal,
we should always have at lease points as candidates at each time point.

```py
class Solution:
    def isPossibleToCutPath(self, A: List[List[int]]) -> bool:
        m, n = len(A), len(A[0])
        for r in range(m):
            for c in range(n):
                if r == c == 0 or A[r][c] == 0:
                    continue
                if (r == 0 or A[r - 1][c] == 0) and (c == 0 and A[r][c - 1] == 0):
                    A[r][c] = 0

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == m - 1 and c == n - 1) or A[r][c] == 0:
                    continue
                if (r == m - 1 or A[r + 1][c] == 0) and (c == n - 1 or A[r][c + 1] == 0):
                    A[r][c] = 0

        count = Counter(r + c for r in range(m) for c in range(n) if A[r][c])
        return any(count[i] < 2 for i in range(1, n + m - 2))
```
</details>