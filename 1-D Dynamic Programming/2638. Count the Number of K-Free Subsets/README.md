[2638. Count the Number of K-Free Subsets](https://leetcode.com/problems/count-the-number-of-k-free-subsets/)

`Medium`

You are given an integer array `nums`, which contains **distinct** elements and an integer `k`.

A subset is called a **k-Free** subset if it contains **no** two elements with an absolute difference equal to `k`. Notice that the empty set is a **k-Free** subset.

Return the number of **k-Free** subsets of `nums`

A subset of an array is a selection of elements (possibly none) of the array.

```
Example 1:

Input: nums = [5,4,6], k = 1
Output: 5
Explanation: There are 5 valid subsets: {}, {5}, {4}, {6} and {4,6}

Example 2:
Input: nums = [10, 5, 9, 11], k = 20
Output: 16
Explanation: All subsets are valid. Since total number of subsets is 2^4=16, so the answer is 16.
```

Constraints
- 1 <= nums.length <= 50
- 1 <= nums[i] <= 1000
- 1 <= k <= 1000

<details>
<summary>Video Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=qw0OVFVg5ng)
</details>