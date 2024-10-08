[1901. Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/)

`Medium`

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

```
Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
``` 

Constraints:

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 500
- 1 <= mat[i][j] <= 10^5
- No two adjacent cells are equal.

Accepted
85.2K
Submissions
163.5K
Acceptance Rate
52.1%

<details>
<summary>Hint 1</summary>

Let's assume that the width of the array is bigger than the height, otherwise, we will split in another direction.

</details>
<details>
<summary>Hint 2</summary>

Split the array into three parts: central column left side and right side.

</details>
<details>
<summary>Hint 3</summary>

Go through the central column and two neighbor columns and look for maximum.

</details>
<details>
<summary>Hint 4</summary>

If it's in the central column - this is our peak.

</details>
<details>
<summary>Hint 5</summary>

If it's on the left side, run this algorithm on subarray left_side + central_column.

</details>
<details>
<summary>Hint 6</summary>

If it's on the right side, run this algorithm on subarray right_side + central_column

</details>