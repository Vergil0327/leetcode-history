[1711. Count Good Meals](https://leetcode.com/problems/count-good-meals/)

`Medium`

A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 10^9 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.

```
Example 1:
Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

Example 2:
Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
``` 

Constraints:

- 1 <= deliciousness.length <= 10^5
- 0 <= deliciousness[i] <= 2^20

Accepted
41.9K
Submissions
136.1K
Acceptance Rate
30.8%

<details>
<summary>Hint 1</summary>

Note that the number of powers of 2 is at most 21 so this turns the problem to a classic find the number of pairs that sum to a certain value but for 21 values

</details>
<details>
<summary>Hint 2</summary>

You need to use something fasters than the NlogN approach since there is already the log of iterating over the powers so one idea is two pointers

</details>