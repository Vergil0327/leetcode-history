[1124. Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/description/)

`Medium`

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

```
Example 1:
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].

Example 2:
Input: hours = [6,6,6]
Output: 0
``` 

Constraints:

- 1 <= hours.length <= 10^4
- 0 <= hours[i] <= 16

Acceptance Rate
34.6%

<details>
<summary>Hint 1</summary>

Make a new array A of +1/-1s corresponding to if hours[i] is > 8 or not. The goal is to find the longest subarray with positive sum.

</details>

<details>
<summary>Hint 2</summary>

Using prefix sums (PrefixSum[i+1] = A[0] + A[1] + ... + A[i]), you need to find for each j, the smallest i < j with PrefixSum[i] + 1 == PrefixSum[j].

</details>

<details>
<summary>Video Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=SKZZRIhh4M0)
</details>