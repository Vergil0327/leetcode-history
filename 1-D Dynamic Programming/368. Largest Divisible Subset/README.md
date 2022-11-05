[368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)

`Medium`

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

```
Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
```

Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2 * 10^9
- All the integers in nums are unique.

<details>
<summary>Hint 1</summary>

think LIS. (longest increasing subsequence)
</details>

<details>
<summary>Hint 2</summary>

divisibility is transitive, a multiple x of some divisor nums[i] is also a multiple of all elements in nums, so it's not necessary to explicitly test divisibility of x by all elements in nums.

8%4==0
4%2==0
don't need to check 8%2 if we sort the array to avoid we do something like 4%8
4%8==0
3%8==0
2%8==0
</details>

<details>
<summary>Hint 3</summary>

use another array to tracks our update path of DP
</details>

<details>
<summary>Video Explanation</summary>

[here](https://www.youtube.com/watch?v=hrwP6I5v1XY)
</details>

