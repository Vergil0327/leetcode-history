[931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/description/)

`Medium`

Given an n x n array of integers matrix, return the **minimum sum** of any **falling path** through matrix.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

```
Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

Constraints:

- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- -100 <= matrix[i][j] <= 100

<details>
<summary>Explanation</summary>

[labuladong](https://labuladong.github.io/article/?qno=931)

對於 matrix[i][j]，只可能從 matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1] 这三个位置轉移過來

dp 函數的定義：從First Row（matrix[0][..]）向下落，落到位置 matrix[i][j] 的最小路徑和為 dp(matrix,i, j)，因此答案就是：

```
min(
    dp(matrix, i - 1, j),
    dp(matrix, i - 1, j - 1),
    dp(matrix, i - 1, j + 1)
)
```

</details>