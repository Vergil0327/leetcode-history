[1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/description/)

`Medium`

*same as [1020. Number of Enclaves](../1020.%20Number%20of%20Enclaves/)*

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

```
Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
``` 

Constraints:

- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <=1

<details>
<summary>Hint 1</summary>

Exclude connected group of 0s on the corners because they are not closed island.
</details>

<details>
<summary>Hint 2</summary>

Return number of connected component of 0s on the grid.
</details>
