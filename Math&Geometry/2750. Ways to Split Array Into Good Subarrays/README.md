[2750. Ways to Split Array Into Good Subarrays](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/)

`Medium`

You are given a binary array nums.

A subarray of an array is good if it contains exactly one element with the value 1.

Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

```
Example 1:
Input: nums = [0,1,0,0,1]
Output: 3
Explanation: There are 3 ways to split nums into good subarrays:
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]

Example 2:
Input: nums = [0,1,0]
Output: 1
Explanation: There is 1 way to split nums into good subarrays:
- [0,1,0]
``` 

Constraints:

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 1

Acceptance Rate
28.4%

<details>
<summary>Hint 1</summary>

If the array consists of only 0s answer is 0.

</details>

<details>
<summary>Hint 2</summary>

In the final split, exactly one separation point exists between two consecutive 1s.

</details>

<details>
<summary>Hint 3</summary>

In how many ways can separation points be put?

</details>