[3640. Trionic Array II](https://leetcode.com/problems/trionic-array-ii/)

`Hard`

You are given an integer array nums of length n.

A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

nums[l...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...r] is strictly increasing.
Return the maximum sum of any trionic subarray in nums.

```
Example 1:
Input: nums = [0,-2,-1,-3,0,2,-1]
Output: -4
Explanation:

Pick l = 1, p = 2, q = 3, r = 5:

nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.

Example 2:
Input: nums = [1,4,2,7]
Output: 14
Explanation:

Pick l = 0, p = 1, q = 2, r = 3:

nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
Sum = 1 + 4 + 2 + 7 = 14.
```

Constraints:

- 4 <= n = nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Accepted
2,743/17.8K
Acceptance Rate
15.4%

<details>
<summary>Hint 1</summary>

Use dynamic programming

</details>
<details>
<summary>Hint 2</summary>

Let four arrays dp0...dp3 where dpk[i] is the max sum of a subarray ending at i after finishing k of the four phases (start -> inc -> dec -> inc)

</details>
<details>
<summary>Hint 3</summary>

Process each i>0

</details>
<details>
<summary>Hint 4</summary>

If nums[i]>nums[i‑1], set dp1[i]=max(dp1[i‑1]+nums[i], dp0[i‑1]+nums[i]), dp3[i]=max(dp3[i‑1]+nums[i], dp2[i‑1]+nums[i])

</details>
<details>
<summary>Hint 5</summary>

If nums[i], set dp2[i]=max(dp2[i‑1]+nums[i], dp1[i‑1]+nums[i])

</details>
<details>
<summary>Hint 6</summary>

Always carry over dp0[i]=dp0[i‑1]+nums[i] when nums[i]>nums[i‑1]

</details>

<details>
<summary>Hint 7</summary>

Return the maximum value in dp3

</details>