[2376. Count Special Integers](https://leetcode.com/problems/count-special-integers/description/)

`Hard`

We call a positive integer special if all of its digits are distinct.

Given a positive integer n, return the number of special integers that belong to the interval [1, n].

```
Example 1:
Input: n = 20
Output: 19
Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.

Example 2:
Input: n = 5
Output: 5
Explanation: All the integers from 1 to 5 are special.

Example 3:
Input: n = 135
Output: 110
Explanation: There are 110 integers from 1 to 135 that are special.
Some of the integers that are not special are: 22, 114, and 131.
``` 

Constraints:

- 1 <= n <= 2 * 10^9

Accepted
10.2K
Submissions
27.2K
Acceptance Rate
37.7%

<details>
<summary>Hint 1</summary>

Try to think of dynamic programming.

</details>
<details>
<summary>Hint 2</summary>

Use the idea of digit dynamic programming to build the numbers, in addition to a bitmask that will tell which digits you have used so far on the number that you are building.

</details>