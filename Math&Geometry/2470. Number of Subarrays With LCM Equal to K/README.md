[2470. Number of Subarrays With LCM Equal to K](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/submissions/)

`Medium`

Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

```
Example 1:
Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]

Example 2:
Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
```

*Follow-up [Find Number of Subarrays With GCD Equal to K](../2447.%20Number%20of%20Subarrays%20With%20GCD%20Equal%20to%20K/)*

Constraints:

- 1 <= nums.length <= 1000
- 1 <= nums[i], k <= 1000

<details>
<summary>Hint 2</summary>

The constraints on nums.length are small. It is possible to check every subarray.
</details>

<details>
<summary>Hint 2</summary>

To calculate LCM, you can use a built-in function or the formula lcm(a, b) = a * b / gcd(a, b).
</details>

<details>
<summary>Hint 3</summary>

As you calculate the LCM of more numbers, it can only become greater. Once it becomes greater than k, you know that any larger subarrays containing all the current elements will not work.
</details>