[1425. Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/description/)

`Hard`

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

```
Example 1:
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].

Example 2:
Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.

Example 3:
Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
``` 

Constraints:

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Acceptance Rate
47.7%

<details>
<summary>Hint 1</summary>

Use dynamic programming.

</details>
<details>
<summary>Hint 2</summary>

Let dp[i] be the solution for the prefix of the array that ends at index i, if the element at index i is in the subsequence.

</details>
<details>
<summary>Hint 3</summary>

dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1])

</details>
<details>
<summary>Hint 4</summary>

Use a heap with the sliding window technique to optimize the dp.

</details>