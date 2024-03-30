[3098. Find the Sum of Subsequence Powers](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/)

`Hard`

You are given an integer array nums of length n, and a positive integer k.

The power of a 
subsequence
 is defined as the minimum absolute difference between any two elements in the subsequence.

Return the sum of powers of all subsequences of nums which have length equal to k.

Since the answer may be large, return it modulo 109 + 7.

```
Example 1:
Input: nums = [1,2,3,4], k = 3
Output: 4
Explanation:

There are 4 subsequences in nums which have length 3: [1,2,3], [1,3,4], [1,2,4], and [2,3,4]. The sum of powers is |2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4.

Example 2:
Input: nums = [2,2], k = 2
Output: 0
Explanation:

The only subsequence in nums which has length 2 is [2,2]. The sum of powers is |2 - 2| = 0.

Example 3:
Input: nums = [4,3,-1], k = 2
Output: 10
Explanation:

There are 3 subsequences in nums which have length 2: [4,3], [4,-1], and [3,-1]. The sum of powers is |4 - 3| + |4 - (-1)| + |3 - (-1)| = 10.
```

Constraints:

- 2 <= n == nums.length <= 50
- -10^8 <= nums[i] <= 10^8 
- 2 <= k <= n

Accepted
212
Submissions
3.7K
Acceptance Rate
5.8%

<details>
<summary>Hint 1</summary>

Sort nums.

</details>
<details>
<summary>Hint 2</summary>

There are at most n2 distinct differences.

</details>
<details>
<summary>Hint 3</summary>

For a particular difference d, let dp[len][i][j] be the number of subsequences of length len in the subarray nums[0..i] where the last element picked was at index j.

</details>
<details>
<summary>Hint 4</summary>

For each index, we can check if it can be picked if nums[i] - nums[j] <= d.

</details>