[3729. Count Distinct Subarrays Divisible by K in Sorted Array](https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/)

`Hard`

You are given an integer array nums sorted in non-descending order and a positive integer k.

A subarray of nums is good if the sum of its elements is divisible by k.

Return an integer denoting the number of distinct good subarrays of nums.

Subarrays are distinct if their sequences of values are. For example, there are 3 distinct subarrays in [1, 1, 1], namely [1], [1, 1], and [1, 1, 1].

```
Example 1:
Input: nums = [1,2,3], k = 3
Output: 3
Explanation:

The good subarrays are [1, 2], [3], and [1, 2, 3]. For example, [1, 2, 3] is good because the sum of its elements is 1 + 2 + 3 = 6, and 6 % k = 6 % 3 = 0.

Example 2:
Input: nums = [2,2,2,2,2,2], k = 6
Output: 2
Explanation:

The good subarrays are [2, 2, 2] and [2, 2, 2, 2, 2, 2]. For example, [2, 2, 2] is good because the sum of its elements is 2 + 2 + 2 = 6, and 6 % k = 6 % 6 = 0.

Note that [2, 2, 2] is counted only once.
```

Constraints:

- 1 <= nums.length <= $10^5$
- 1 <= nums[i] <= $10^9$
- nums is sorted in non-descending order.
- 1 <= k <= $10^9$
 

Accepted
2,706/12.8K
Acceptance Rate
21.1%

<details>
<summary>Hint 1</summary>

Use prefix sums.

</details>
<details>
<summary>Hint 2</summary>

Any subarray with >= 2 distinct values has a unique strict-increase boundary (i, j), so the value sequence is identified by that boundary and how many elements you take from each edge.

</details>
<details>
<summary>Hint 3</summary>

Count single-value sequences per run by testing (L*val) % k == 0.

</details>