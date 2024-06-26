[2209. Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/)

`Hard`

You are given a **0-indexed binary** string `floor`, which represents the colors of tiles on a floor:

- `floor[i] = '0'` denotes that the ith tile of the floor is colored black.
- On the other hand, `floor[i] = '1'` denotes that the ith tile of the floor is colored white.

You are also given `numCarpets` and `carpetLen`. You have `numCarpets` black carpets, each of length `carpetLen` tiles. Cover the tiles with the given carpets such that the number of white tiles still visible is minimum. Carpets may overlap one another.

Return the minimum number of white tiles still visible.

Example 1:

![ex1](ex1.png)

Input: floor = "10110101", numCarpets = 2, carpetLen = 2
Output: 2
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.

Example 2:

![ex2](ex2.png)

Input: floor = "11111", numCarpets = 2, carpetLen = 3
Output: 0
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.


Constraints:

- 1 <= carpetLen <= floor.length <= 1000
- floor[i] is either '0' or '1'.
- 1 <= numCarpets <= 1000

<details>
<summary>Hint 1</summary>

Can you think of a DP solution?

</details>

<details>
<summary>Hint 2</summary>

Let DP[i][j] denote the minimum number of white tiles still visible from indices i to floor.length-1 after covering with at most j carpets.

</details>

<details>
<summary>Hint 3</summary>

The transition will be whether to put down the carpet at position i (if possible), or not.

</details>

<details>
<summary>Video Solution</summary>

[HuifengGuan](https://www.youtube.com/watch?v=ZvXp0_vgn2Q&ab_channel=HuifengGuan)
</details>