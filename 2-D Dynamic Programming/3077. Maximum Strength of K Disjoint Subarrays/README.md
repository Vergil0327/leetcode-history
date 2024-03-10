[3077. Maximum Strength of K Disjoint Subarrays](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/)

`Hard`

You are given a 0-indexed array of integers nums of length n, and a positive odd integer k.

The strength of x subarrays is defined as strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1 where sum[i] is the sum of the elements in the ith subarray. Formally, strength is sum of (-1)i+1 * sum[i] * (x - i + 1) over all i's such that 1 <= i <= x.

You need to select k disjoint 
subarrays
 from nums, such that their strength is maximum.

Return the maximum possible strength that can be obtained.

Note that the selected subarrays don't need to cover the entire array.

```
Example 1:
Input: nums = [1,2,3,-1,2], k = 3
Output: 22
Explanation: The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is (1 + 2 + 3) * 3 - (-1) * 2 + 2 * 1 = 22.

Example 2:
Input: nums = [12,-2,-2,-2,-2], k = 5
Output: 64
Explanation: The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..1], nums[2..2], nums[3..3], and nums[4..4]. The strength is 12 * 5 - (-2) * 4 + (-2) * 3 - (-2) * 2 + (-2) * 1 = 64.

Example 3:
Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The best possible way to select 1 subarray is: nums[0..0]. The strength is -1.
``` 

Constraints:

- 1 <= n <= 10^4
- -10^9 <= nums[i] <= 10^9
- 1 <= k <= n
- 1 <= n * k <= 10^6
- k is odd.

Accepted
2.1K
Submissions
10.5K
Acceptance Rate
19.6%

<details>
<summary>Hint 1</summary>

Let dp[i][j][x == 0/1] be the maximum strength to select j disjoint subarrays from the original array’s suffix (nums[i..(n - 1)]), x denotes whether we select the element or not.

</details>
<details>
<summary>Hint 2</summary>

Initially dp[n][0][0] == 0.

</details>
<details>
<summary>Hint 3</summary>

We have dp[i][j][1] = nums[i] * get(j) + max(dp[i + 1][j - 1][0], dp[i + 1][j][1]) where get(j) = j if j is odd, otherwise -j.

</details>
<details>
<summary>Hint 4</summary>

We can select nums[i] as a separate subarray or select at least nums[i] and nums[i + 1] as the first subarray. dp[i][j][0] = max(dp[i + 1][j][0], dp[i][j][1]).

</details>
<details>
<summary>Hint 5</summary>

The answer is dp[0][k][0].

</details>