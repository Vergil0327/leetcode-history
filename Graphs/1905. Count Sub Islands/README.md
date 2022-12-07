[1905. Count Sub Islands](https://leetcode.com/problems/count-sub-islands/description/)

`Medium`

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

```
Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
```

Constraints:

- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 500
- grid1[i][j] and grid2[i][j] are either 0 or 1.

<details>
<summary>Hint 1</summary>

Let's use floodfill to iterate over the islands of the second grid
</details>

<details>
<summary>Hint 2</summary>

Let's note that if all the cells in an island in the second grid if they are represented by land in the first grid then they are connected hence making that island a sub-island
</details>

<details>
<summary>Lee215 Solution</summary>

```c++
    int countSubIslands(vector<vector<int>>& B, vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size(), res = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (A[i][j] == 1)
                    res += dfs(B, A, i, j);
        return res;
    }


    int dfs(vector<vector<int>>& B, vector<vector<int>>& A, int i, int j) {
        int m = A.size(), n = A[0].size(), res = 1;
        if (i < 0 || i == m || j < 0 || j == n || A[i][j] == 0) return 1;
        A[i][j] = 0;
        res &= dfs(B, A, i - 1, j);
        res &= dfs(B, A, i + 1, j);
        res &= dfs(B, A, i, j - 1);
        res &= dfs(B, A, i, j + 1);
        return res & B[i][j];
    }
```

```python
    def countSubIslands(self, B, A):
        n, m = len(A), len(A[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and A[i][j] == 1): return 1
            A[i][j] = 0
            res = B[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res &= dfs(i + di, j + dj)
            return res
            
        return sum(dfs(i, j) for i in xrange(n) for j in xrange(m) if A[i][j])
```
</details>