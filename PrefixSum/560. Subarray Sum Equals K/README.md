[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

`Medium`

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

```
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
```

Constraints:

- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

<details>
<summary>Hint 1</summary>

Will Brute force work here? Try to optimize it.
</details>

<details>
<summary>Hint 2</summary>

Can we optimize it by using some extra space?
</details>

<details>
<summary>Hint 3</summary>

What about storing sum frequencies in a hash table? Will it be useful?
</details>

<details>
<summary>Hint 4</summary>

sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
</details>