[2447. Number of Subarrays With GCD Equal to K](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/)

`Medium`

Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

```
Example 1:
Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]

Example 2:
Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.
```

Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i], k <= 10^9

*Follow-Up [Find Number of Subarrays With LCM Equal to K](../2470.%20Number%20of%20Subarrays%20With%20LCM%20Equal%20to%20K/)*

<details>
<summary>Hint 1</summary>

The constraints on nums.length are small. It is possible to check every subarray.
</details>

<details>
<summary>Hint 2</summary>

To calculate GCD, you can use a built-in function or the Euclidean Algorithm.
</details>