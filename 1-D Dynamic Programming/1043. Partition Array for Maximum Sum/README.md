[1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/)

`Medium`

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

```
Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:
Input: arr = [1], k = 1
Output: 1
```

Constraints:

- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^9
- 1 <= k <= arr.length

<details>
<summary>Hint 1</summary>

Think dynamic programming: dp[i] will be the answer for array A[0], ..., A[i-1].
</details>

<details>
<summary>Hint 2</summary>

For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .
</details>

<details>
<summary>Video Explanation</summary>

[Huifeng Guan - 1043 Partition Array for Maximum Sum](https://www.youtube.com/watch?v=Zd00uagpi4U)
</details>