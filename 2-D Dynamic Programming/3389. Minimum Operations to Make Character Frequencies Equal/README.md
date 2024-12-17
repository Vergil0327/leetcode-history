[3389. Minimum Operations to Make Character Frequencies Equal](https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/)

`Hard`

You are given a string s.

A string t is called good if all characters of t occur the same number of times.

You can perform the following operations any number of times:

- Delete a character from s.
- Insert a character in s.
- Change a character in s to its next letter in the alphabet.
Note that you cannot change 'z' to 'a' using the third operation.

Return the minimum number of operations required to make s good.

```
Example 1:
Input: s = "acab"
Output: 1
Explanation:
We can make s good by deleting one occurrence of character 'a'.

Example 2:
Input: s = "wddw"
Output: 0
Explanation:
We do not need to perform any operations since s is initially good.

Example 3:
Input: s = "aaabc"
Output: 2
Explanation:
We can make s good by applying these operations:
Change one occurrence of 'a' to 'b'
Insert one occurrence of 'c' into s
```

Constraints:

- 3 <= s.length <= 2 * 10^4
- s contains only lowercase English letters.

Accepted
1.1K
Submissions
7.2K
Acceptance Rate
15.0%

<details>
<summary>Hint 1</summary>

The order of the letters in the string is irrelevant.

</details>
<details>
<summary>Hint 2</summary>

Compute an occurrence array occ where occ[x] is the number of occurrences of the x character of the alphabet. How do the described operations change occ?

</details>
<details>
<summary>Hint 3</summary>

We have three types of operations: increase any occ[x] by 1, decrease any occ[x] by 1, or decrease any occ[x] by 1 and simultaneously increase occ[x + 1] by 1 at the same time. To make s good, we need to make occ good. occ is good if and only if every occ[x] equals either 0 or some constant c.

</details>
<details>
<summary>Hint 4</summary>

If you know the value of c, how can you calculate the minimum operations required to make occ good?

</details>
<details>
<summary>Hint 5</summary>

Observation 1: It is never optimal to apply the third type of operation (simultaneous decrease and increase) on two continuous elements occ[x] and occ[x + 1]. Instead, we can decrease occ[x] by 1 then increase occ[x + 2] by 1 to achieve the same effect.

</details>
<details>
<summary>Hint 6</summary>

Observation 2: It is never optimal to increase an element of occ then decrease it, or vice versa.

</details>
<details>
<summary>Hint 7</summary>

Use dynamic programming where dp[i] is the minimum number of operations required to make occ[0..i] good. You will need to use the above observations to come up with the transitions.

</details>