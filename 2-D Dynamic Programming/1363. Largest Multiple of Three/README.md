[1363. Largest Multiple of Three](https://leetcode.com/problems/largest-multiple-of-three/description/)

`Hard`

Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.

```
Example 1:
Input: digits = [8,1,9]
Output: "981"

Example 2:
Input: digits = [8,6,7,1,0]
Output: "8760"

Example 3:
Input: digits = [1]
Output: ""
```

Constraints:

- 1 <= digits.length <= 10^4
- 0 <= digits[i] <= 9

<details>
<summary>Hint 1</summary>

A number is a multiple of three if and only if its sum of digits is a multiple of three.

</details>

<details>
<summary>Hint 2</summary>

Use dynamic programming.

</details>

<details>
<summary>Hint 3</summary>

To find the maximum number, try to maximize the number of digits of the number.

</details>

<details>
<summary>Hint 4</summary>

Sort the digits in descending order to find the maximum number.

</details>