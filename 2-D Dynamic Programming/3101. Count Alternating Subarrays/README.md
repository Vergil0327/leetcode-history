[3101. Count Alternating Subarrays](https://leetcode.com/problems/count-alternating-subarrays/)

`Medium`

You are given a **binary array** nums.
> A binary array is an array which contains only 0 and 1.

We call a subarray **alternating** if no two adjacent elements in the subarray have the same value.
> A subarray is a contiguous non-empty sequence of elements within an array.

Return the number of alternating subarrays in nums.

```
Example 1:
Input: nums = [0,1,1,1]
Output: 5
Explanation:
The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

Example 2:
Input: nums = [1,0,1,0]
Output: 10
Explanation:
Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.
```

Constraints:

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Accepted
14.3K
Submissions
28K
Acceptance Rate
51.0%

<details>
<summary>Hint 1</summary>

Try using dynamic programming.

</details>
<details>
<summary>Hint 2</summary>

Let dp[i] be the number of alternating subarrays ending at index i.

</details>
<details>
<summary>Hint 3</summary>

The final answer is the sum of dp[i] over all indices i from 0 to n - 1.

</details>