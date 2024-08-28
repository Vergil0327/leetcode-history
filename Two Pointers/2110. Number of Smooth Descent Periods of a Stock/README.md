[2110. Number of Smooth Descent Periods of a Stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/)

`Medium`

You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

```
Example 1:
Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.

Example 2:
Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.

Example 3:
Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]
``` 

Constraints:

- 1 <= prices.length <= 10^5
- 1 <= prices[i] <= 10^5

Accepted
38.1K
Submissions
64.3K
Acceptance Rate
59.2%

<details>
<summary>Hint 1</summary>

Any array is a series of adjacent longest possible smooth descent periods. For example, [5,3,2,1,7,6] is [5] + [3,2,1] + [7,6].

</details>
<details>
<summary>Hint 2</summary>

Think of a 2-pointer approach to traverse the array and find each longest possible period.

</details>
<details>
<summary>Hint 3</summary>

Suppose you found the longest possible period with a length of k. How many periods are within that period? How can you count them quickly? Think of the formula to calculate the sum of 1, 2, 3, ..., k.

</details>