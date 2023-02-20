[718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)

`Medium`

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

```
Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
```

Constraints:

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 100

<details>
<summary>Hint 1</summary>

Use dynamic programming. dp[i][j] will be the longest common prefix of A[i:] and B[j:].
</details>

<details>
<summary>Hint 2</summary>

The answer is max(dp[i][j]) over all i, j.
</details>