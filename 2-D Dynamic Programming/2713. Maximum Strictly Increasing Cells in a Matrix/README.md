[2713. Maximum Strictly Increasing Cells in a Matrix](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/description/)

`Hard`

Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.

From the starting cell, you can move to any other cell in the same row or column, but only if the value of the destination cell is strictly greater than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.

Return an integer denoting the maximum number of cells that can be visited.

```
Example 1:
Input: mat = [[3,1],[3,4]]
Output: 2
Explanation: The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2. 

Example 2:
Input: mat = [[1,1],[1,1]]
Output: 1
Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example. 

Example 3:
Input: mat = [[3,1,6],[-9,5,7]]
Output: 4
Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4. 
``` 

Constraints:

- m == mat.length 
- n == mat[i].length 
- 1 <= m, n <= 10^5
- 1 <= m * n <= 10^5
- -10^5 <= mat[i][j] <= 10^5

Acceptance Rate
14.7%

<details>
<summary>Hint 1</summary>

We can try to build the answer in a bottom-up fashion, starting from the smallest values and increasing to the larger values.

</details>

<details>
<summary>Hint 2</summary>

Going through the values in sorted order, we can store the maximum path we have seen so far for a row/column.

</details>

<details>
<summary>Hint 3</summary>

When we are at a cell, we check its row and column to find out the best previous smaller value that we’ve got so far, and we use it to increment the current value of the row and column.

</details>