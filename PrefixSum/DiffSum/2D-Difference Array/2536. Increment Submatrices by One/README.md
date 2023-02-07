[2536. Increment Submatrices by One](https://leetcode.com/contest/weekly-contest-328/problems/increment-submatrices-by-one/)

`Medium`

You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

```
Example 1:
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

Example 2:
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
```

Constraints:

- 1 <= n <= 500
- 1 <= queries.length <= 10^4
- 0 <= row1i <= row2i < n
- 0 <= col1i <= col2i < n

<details>
<summary>Hint 1</summary>

Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.

</details>

<details>
<summary>Hint 2</summary>

For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].

</details>

<details>
<summary>Hint 3</summary>

After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].

</details>

<details>
<summary>Explanation</summary>

[[Python3] Sweep Line (Range Addition w/ Visualization), Clean & Concise](https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-w-visualization-clean-concise/?orderBy=most_votes)

[HuifengGuan](https://www.youtube.com/watch?v=J2TUaneNk90)
</details>