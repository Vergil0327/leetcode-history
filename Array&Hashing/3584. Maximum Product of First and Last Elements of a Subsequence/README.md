[3584. Maximum Product of First and Last Elements of a Subsequence](https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/)

`Medium`

You are given an integer array nums and an integer m.

Return the maximum product of the first and last elements of any subsequence of nums of size m.

```
Example 1:
Input: nums = [-1,-9,2,3,-2,-3,1], m = 1
Output: 81
Explanation:

The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore, the answer is 81.

Example 2:
Input: nums = [1,3,-5,5,6,-4], m = 3
Output: 20
Explanation:
The subsequence [-5, 6, -4] has the largest product of the first and last elements.

Example 3:
Input: nums = [2,-1,2,-6,5,2,-5,7], m = 2
Output: 35
Explanation:
The subsequence [5, 7] has the largest product of the first and last elements.
```

Constraints:

- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= m <= nums.length

Accepted
10,841/38K
Acceptance Rate
28.5%

<details>
<summary>Hint 1</summary>

We can select nums[i] as the first element of the subsequence, and the last one can be any of nums[i + m - 1], nums[i + m], ..., nums[n - 1].

</details>
<details>
<summary>Hint 2</summary>

If we select the first element from the largest i, the suffix just gets longer, and we can update the minimum and maximum values dynamically.

</details>