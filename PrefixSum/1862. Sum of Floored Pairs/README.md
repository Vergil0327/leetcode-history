[1862. Sum of Floored Pairs](https://leetcode.com/problems/sum-of-floored-pairs/)

`Hard`

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 10^9 + 7.

The floor() function returns the integer part of the division.

```
Example 1:
Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.

Example 2:
Input: nums = [7,7,7,7,7,7,7]
Output: 49
``` 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Accepted
8.3K
Submissions
29.2K
Acceptance Rate
28.6%

<details>
<summary>Hint 1</summary>

Find the frequency (number of occurrences) of all elements in the array.

</details>
<details>
<summary>Hint 2</summary>

For each element, iterate through its multiples and multiply frequencies to find the answer.

</details>
<details>
<summary>Great Explanation by @HuifengGuan in Chinese</summary>

[Youtube Video](https://www.youtube.com/watch?v=OM6oph-bDhE&ab_channel=HuifengGuan)

</details>
