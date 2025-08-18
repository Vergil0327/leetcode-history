[3649. Number of Perfect Pairs](https://leetcode.com/problems/number-of-perfect-pairs/)

`Medium`

You are given an integer array nums.

A pair of indices (i, j) is called perfect if the following conditions are satisfied:

i < j
Let a = nums[i], b = nums[j]. Then:
min(|a - b|, |a + b|) <= min(|a|, |b|)
max(|a - b|, |a + b|) >= max(|a|, |b|)
Return the number of distinct perfect pairs.

Note: The absolute value |x| refers to the non-negative value of x.

```
Example 1:
Input: nums = [0,1,2,3]
Output: 2
Explanation:
There are 2 perfect pairs:

(i, j)	(a, b)	min(|a − b|, |a + b|)	min(|a|, |b|)	max(|a − b|, |a + b|)	max(|a|, |b|)
(1, 2)	(1, 2)	min(|1 − 2|, |1 + 2|) = 1	1	max(|1 − 2|, |1 + 2|) = 3	2
(2, 3)	(2, 3)	min(|2 − 3|, |2 + 3|) = 1	2	max(|2 − 3|, |2 + 3|) = 5	3

Example 2:
Input: nums = [-3,2,-1,4]
Output: 4
Explanation:
There are 4 perfect pairs:

(i, j)	(a, b)	min(|a − b|, |a + b|)	min(|a|, |b|)	max(|a − b|, |a + b|)	max(|a|, |b|)
(0, 1)	(-3, 2)	min(|-3 - 2|, |-3 + 2|) = 1	2	max(|-3 - 2|, |-3 + 2|) = 5	3
(0, 3)	(-3, 4)	min(|-3 - 4|, |-3 + 4|) = 1	3	max(|-3 - 4|, |-3 + 4|) = 7	4
(1, 2)	(2, -1)	min(|2 - (-1)|, |2 + (-1)|) = 1	1	max(|2 - (-1)|, |2 + (-1)|) = 3	2
(1, 3)	(2, 4)	min(|2 - 4|, |2 + 4|) = 2	2	max(|2 - 4|, |2 + 4|) = 6	4

Example 3:
Input: nums = [1,10,100,1000]
Output: 0
Explanation:

There are no perfect pairs. Thus, the answer is 0.
```

Constraints:

- 2 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Accepted
14,263/50K
Acceptance Rate
28.5%

<details>
<summary>Hint 1</summary>

For any pair (a, b), let x = |a| and y = |b| and assume x <= y; the two conditions simplify to y <= 2*x.

</details>
<details>
<summary>Hint 2</summary>

Sort the array by absolute value.

</details>
<details>
<summary>Hint 3</summary>

Maintain two pointers i and j (starting at 0 and 1): for each i, advance j while abs(nums[j]) <= 2*abs(nums[i]).

</details>
<details>
<summary>Hint 4</summary>

For each i, add j - i - 1 to your answer.

</details>