[4109. Count Valid Suffix Sorts II](https://leetcode.com/problems/count-valid-suffix-sorts-ii/)

`Hard`

You are given two integer arrays nums and target of lengths n and m, respectively, where n <= m.

For each index i, consider sorting the suffix nums[i..n - 1] of the original array in non-increasing order.

Return an integer array ans of length m - n + 1, where ans[k] is the number of indices i for which the resulting array equals target[k..k + n - 1].

A subarray is a contiguous non-empty sequence of elements within an array.

A suffix of an array is a subarray that begins at any index and extends to its end.


Example 1:
Input: nums = [2,2,3], target = [2,2,3,2,1,3,2,2]
Output: [1,1,0,0,0,1]
Explanation:

Sorting the suffix starting at indices 0, 1, and 2 produces [3, 2, 2], [2, 3, 2], and [2, 2, 3], respectively.

k = 0: [2, 2, 3] is produced by i = 2.
k = 1: [2, 3, 2] is produced by i = 1.
k = 2, 3, 4: None of the corresponding subarrays can be produced.
k = 5: [3, 2, 2] is produced by i = 0.
Therefore, the answer is [1, 1, 0, 0, 0, 1].

Example 2:
Input: nums = [5,6,5], target = [5,6,5,5,6,5]
Output: [2,1,0,2]
Explanation:

Sorting the suffix starting at index 0 produces [6, 5, 5], while starting at either index 1 or 2 produces [5, 6, 5].

k = 0: [5, 6, 5] is produced by i = 1 and i = 2.
k = 1: [6, 5, 5] is produced by i = 0.
k = 2: [5, 5, 6] cannot be produced.
k = 3: [5, 6, 5] is produced by i = 1 and i = 2.
Therefore, the answer is [2, 1, 0, 2].

Constraints:

- n == nums.length
- m == target.length
- 1 <= n <= m <= 10^5
- 1 <= nums[i], target[i] <= 10^5

Accepted
1,718/3.8K
Acceptance Rate
45.8%