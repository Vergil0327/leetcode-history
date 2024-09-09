[3282. Reach End of Array With Max Score](https://leetcode.com/problems/reach-end-of-array-with-max-score/)

`Medium`

You are given an integer array nums of length n.

Your goal is to start at index 0 and reach index n - 1. You can only jump to indices greater than your current index.

The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.

```
Example 1:
Input: nums = [1,3,1,5]
Output: 7
Explanation:

First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:
Input: nums = [4,3,1,3,2]
Output: 16
Explanation:

Jump directly to the last index. The final score is 4 * 4 = 16.
```

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Accepted
15.3K
Submissions
57.4K
Acceptance Rate
26.6%

<details>
<summary>Hint 1</summary>

It can be proven that from each index i, the optimal solution is to jump to the nearest index j > i such that nums[j] > nums[i].
</details>