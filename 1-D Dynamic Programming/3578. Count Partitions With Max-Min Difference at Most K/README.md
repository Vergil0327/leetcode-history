[3578. Count Partitions With Max-Min Difference at Most K](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/)

`Medium`

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

```
Example 1:
Input: nums = [9,4,1,3,7], k = 4
Output: 6
Explanation:
There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]

Example 2:
Input: nums = [3,3,4], k = 0
Output: 2
Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
```

Constraints:

- 2 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^9
- 0 <= k <= 10^9

Accepted
5,713/14.8K
Acceptance Rate
38.5%

<details>
<summary>Hint 1</summary>

Use dynamic programming.

</details>
<details>
<summary>Hint 2</summary>

Let dp[idx] be the count of ways to partition the array with the last partition ending at index idx.

</details>
<details>
<summary>Hint 3</summary>

Try using a sliding window; we can track the minimum and maximum in the window using deques.

</details>