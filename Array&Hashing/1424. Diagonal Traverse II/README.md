[1424. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)

`Medium`

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

[img1](https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png)

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

[img2](https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png)

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i].length <= 10^5
- 1 <= sum(nums[i].length) <= 10^5
- 1 <= nums[i][j] <= 10^5

<details>
<summary>Hint 1</summary>

Notice that numbers with equal sums of row and column indexes belong to the same diagonal.

</details>
<details>
<summary>Hint 2</summary>

Store them in tuples (sum, row, val), sort them, and then regroup the answer.

</details>