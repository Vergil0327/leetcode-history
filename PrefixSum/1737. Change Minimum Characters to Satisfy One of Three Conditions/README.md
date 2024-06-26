[1737. Change Minimum Characters to Satisfy One of Three Conditions](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/description/)

`Medium`

You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

```
Example 1:
Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

Example 2:
Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".
``` 

Constraints:

- 1 <= a.length, b.length <= 10^5
- a and b consist only of lowercase letters.

Acceptance Rate
35.4%

<details>
<summary>Hint 1</summary>

Iterate on each letter in the alphabet, and check the smallest number of operations needed to make it one of the following: the largest letter in a and smaller than the smallest one in b, vice versa, or let a and b consist only of this letter.

</details>

<details>
<summary>Hint 2</summary>

For the first 2 conditions, take care that you can only change characters to lowercase letters, so you can't make 'z' the smallest letter in one of the strings or 'a' the largest letter in one of them.

</details>