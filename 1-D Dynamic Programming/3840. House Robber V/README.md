[3840. House Robber V](https://leetcode.com/problems/house-robber-v/)

`Medium`

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed and is protected by a security system with a color code.

You are given two integer arrays nums and colors, both of length n, where nums[i] is the amount of money in the ith house and colors[i] is the color code of that house.

You cannot rob two adjacent houses if they share the same color code.

Return the maximum amount of money you can rob.

 

Example 1:
Input: nums = [1,4,3,5], colors = [1,1,2,2]
Output: 9
Explanation:

Choose houses i = 1 with nums[1] = 4 and i = 3 with nums[3] = 5 because they are non-adjacent.
Thus, the total amount robbed is 4 + 5 = 9.

Example 2:
Input: nums = [3,1,2,4], colors = [2,3,2,2]
Output: 8
Explanation:

Choose houses i = 0 with nums[0] = 3, i = 1 with nums[1] = 1, and i = 3 with nums[3] = 4.
This selection is valid because houses i = 0 and i = 1 have different colors, and house i = 3 is non-adjacent to i = 1.
Thus, the total amount robbed is 3 + 1 + 4 = 8.

Example 3:
Input: nums = [10,1,3,9], colors = [1,1,1,2]
Output: 22
Explanation:

Choose houses i = 0 with nums[0] = 10, i = 2 with nums[2] = 3, and i = 3 with nums[3] = 9.
This selection is valid because houses i = 0 and i = 2 are non-adjacent, and houses i = 2 and i = 3 have different colors.
Thus, the total amount robbed is 10 + 3 + 9 = 22.
 

Constraints:

- 1 <= n == nums.length == colors.length <= $10^5$
- 1 <= nums[i], colors[i] <= $10^5$
 

Accepted
27,529/50.8K
Acceptance Rate
54.2%

<details>
<summary>Hint 1</summary>

Use dynamic programming

</details>
<details>
<summary>Hint 2</summary>

Let dp[i] be the maximum money robbable considering houses up to index i

</details>
<details>
<summary>Hint 3</summary>

Initialize dp[i] with nums[i], then compare with skipping the house: dp[i - 1]

</details>
<details>
<summary>Hint 4</summary>

If colors[i] != colors[i - 1], allow taking adjacent house: nums[i] + dp[i - 1]

</details>
<details>
<summary>Hint 5</summary>

Always allow non-adjacent take: nums[i] + dp[i - 2]

</details>
<details>
<summary>Hint 6</summary>

Answer is dp[n - 1]

</details>
