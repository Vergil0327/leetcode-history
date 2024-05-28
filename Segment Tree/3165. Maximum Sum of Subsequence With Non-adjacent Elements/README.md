[3165. Maximum Sum of Subsequence With Non-adjacent Elements](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/)

`Hard`

You are given an array nums consisting of integers. You are also given a 2D array queries, where queries[i] = [posi, xi].

For query i, we first set nums[posi] equal to xi, then we calculate the answer to query i which is the maximum sum of a 
subsequence
 of nums where no two adjacent elements are selected.

Return the sum of the answers to all queries.

Since the final answer may be very large, return it modulo 10^9 + 7.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

```
Example 1:
Input: nums = [3,5,9], queries = [[1,-2],[0,-3]]
Output: 21

Explanation:
After the 1st query, nums = [3,-2,9] and the maximum sum of a subsequence with non-adjacent elements is 3 + 9 = 12.
After the 2nd query, nums = [-3,-2,9] and the maximum sum of a subsequence with non-adjacent elements is 9.

Example 2:
Input: nums = [0,-1], queries = [[0,-5]]
Output: 0
Explanation:
After the 1st query, nums = [-5,-1] and the maximum sum of a subsequence with non-adjacent elements is 0 (choosing an empty subsequence).
```

Constraints:

- 1 <= nums.length <= 5 * 10^4
- -10^5 <= nums[i] <= 10^5
- 1 <= queries.length <= 5 * 10^4
- queries[i] == [posi, xi]
- 0 <= posi <= nums.length - 1
- -10^5 <= xi <= 10^5

Accepted
2.8K
Submissions
21.1K
Acceptance Rate
13.1%

<details>
<summary>Hint 1</summary>

Can you solve each query in O(nums.length) with dynamic programming?

</details>
<details>
<summary>Hint 2</summary>

In order to optimize, we will use segment tree where each node contains the maximum value of (front element has been chosen or not, back element has been chosen or not).

</details>

<details>
<summary>Solution</summary>

[solution by @HuifengGuan](https://www.youtube.com/watch?v=AzzaHQKkwnM&ab_channel=HuifengGuan)

</details>