[3153. Sum of Digit Differences of All Pairs](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/)

`Medium`

You are given an array nums consisting of positive integers where all integers have the same number of digits.

The digit difference between two integers is the count of different digits that are in the same position in the two integers.

Return the sum of the digit differences between all pairs of integers in nums.

```
Example 1:
Input: nums = [13,23,12]
Output: 4

Explanation:
We have the following:
- The digit difference between 13 and 23 is 1.
- The digit difference between 13 and 12 is 1.
- The digit difference between 23 and 12 is 2.
So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.

Example 2:
Input: nums = [10,10,10,10]
Output: 0

Explanation:
All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.
```

Constraints:

- 2 <= nums.length <= 10^5
- 1 <= nums[i] < 10^9
- All integers in nums have the same number of digits.

Accepted
9.5K
Submissions
25.3K
Acceptance Rate
37.3%

<details>
<summary>Hint 1</summary>

You can solve the problem for digits that are on the same position separately, and then sum up all the answers.

</details>
<details>
<summary>Hint 2</summary>

For each position, count the number of occurences of each digit from 0 to 9 that appear on that position.

</details>
<details>
<summary>Hint 3</summary>

Let c be the number of occurences of a digit on a position, that will contribute with c * (n - c) to the final answer, where n is the number of integers in nums.

</details>
