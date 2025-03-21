[3257. Maximum Value Sum by Placing Three Rooks II](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/)

`Hard`

You are given a m x n 2D array board representing a chessboard, where board[i][j] represents the value of the cell (i, j).

Rooks in the same row or column attack each other. You need to place three rooks on the chessboard such that the rooks do not attack each other.

Return the maximum sum of the cell values on which the rooks are placed.

```
Example 1:
Input: board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]
Output: 4
Explanation:
We can place the rooks in the cells (0, 2), (1, 3), and (2, 1) for a sum of 1 + 1 + 2 = 4.

Example 2:
Input: board = [[1,2,3],[4,5,6],[7,8,9]]
Output: 15
Explanation:
We can place the rooks in the cells (0, 0), (1, 1), and (2, 2) for a sum of 1 + 5 + 9 = 15.

Example 3:
Input: board = [[1,1,1],[1,1,1],[1,1,1]]
Output: 3
Explanation:
We can place the rooks in the cells (0, 2), (1, 1), and (2, 0) for a sum of 1 + 1 + 1 = 3.
```
 

Constraints:

- 3 <= m == board.length <= 500
- 3 <= n == board[i].length <= 500
- -10^9 <= board[i][j] <= 10^9


Accepted
2.6K
Submissions
11K
Acceptance Rate
23.4%

<details>
<summary>Hint 1</summary>

Save the top 3 largest values in each row.

</details>
<details>
<summary>Hint 2</summary>

Select any row, and select any of the three values stored in it.

</details>
<details>
<summary>Hint 3</summary>

Get the top 4 values from all of the other 3 largest values of the other rows, which do not share the same column as the selected value.

</details>
<details>
<summary>Hint 4</summary>

Brute force the selection of 2 positions from the top 4 now.

</details>