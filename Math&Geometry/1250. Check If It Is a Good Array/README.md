[1250. Check If It Is a Good Array](https://leetcode.com/problems/check-if-it-is-a-good-array/)

`Hard`

Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

```
Example 1:
Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1

Example 2:
Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1

Example 3:
Input: nums = [3,6]
Output: false
``` 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

Acceptance Rate
58.9%

<details>
<summary>Hint 1</summary>

Eq. ax+by=1 has solution x, y if gcd(a,b) = 1.

</details>

<details>
<summary>Hint 2</summary>

Can you generalize the formula?. Check Bézout's lemma.

</details>