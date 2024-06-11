[3177. Find the Maximum Length of a Good Subsequence II](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/)

`Hard`

You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good if there are at most k indices i in the range [0, seq.length - 2] such that seq[i] != seq[i + 1].

Return the maximum possible length of a good 
subsequence
 of nums.

```
Example 1:
Input: nums = [1,2,1,1,3], k = 2
Output: 4
Explanation:
The maximum length subsequence is [1,2,1,1,3].

Example 2:
Input: nums = [1,2,3,4,5,1], k = 0
Output: 2
Explanation:
The maximum length subsequence is [1,2,3,4,5,1].
```

Constraints:

- 1 <= nums.length <= 5 * 10^3
- 1 <= nums[i] <= 10^9
- 0 <= k <= min(50, nums.length)

Accepted
3.8K
Submissions
19.2K
Acceptance Rate
19.9%

<details>
<summary>Hint 1</summary>

The absolute values in nums don’t really matter. So we can remap the set of values to the range [0, n - 1].

</details>
<details>
<summary>Hint 2</summary>

Let dp[i][j] be the length of the longest subsequence till index j with at most i positions such that seq[i] != seq[i + 1].

</details>
<details>
<summary>Hint 3</summary>

For each value x from left to right, update dp[i][x] = max(dp[i][x] + 1, dp[i - 1][y] + 1), where y != x.

</details>