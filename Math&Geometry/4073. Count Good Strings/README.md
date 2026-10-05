[4073. Count Good Strings](https://leetcode.com/problems/count-good-strings/)

`Hard`

You are given an integer n.

A string is considered good if it consists only of the characters 'a' and 'b', and one of the following holds:

- It contains exactly one distinct character, and its length is odd.
- It can be written as s = s1 + s2, where s1 and s2 are non-empty good strings, and the last character of s1 is different from the first character of s2.
Return the number of good strings of length n, modulo 10^9 + 7.

Here, + denotes string concatenation.


Example 1:
Input: n = 4
Output: 6
Explanation:
The good strings are "aaab", "abbb", "baaa", "bbba", "abab", and "baba".
For example, "aaab" = "aaa" + "b". Both parts are good because each contains one distinct character and has odd length, and their characters at the boundary are different.
Also, "ab" = "a" + "b" is good, so "abab" = "ab" + "ab" is good because the boundary characters are different.
Thus, the answer is 6.

Example 2:
Input: n = 3
Output: 4
Explanation:
The good strings are "aaa", "bbb", "aba", and "bab". Thus, the answer is 4.

Example 3:
Input: n = 2
Output: 2
Explanation:
The good strings are "ab" and "ba". Thus, the answer is 2. 

Constraints:

- 1 <= n <= $10^{15}$

Accepted
4,574/10.1K
Acceptance Rate
45.4%

<details>
<summary>Hint 1</summary>
1a (Fast Doubling): A string is good exactly when every maximal run of identical characters has odd length.
</details>
<details>
<summary>Hint 2</summary>
1b (Fast Doubling): Counting ordered sequences of odd run lengths gives the Fibonacci numbers. Account for the two choices of the first character, then compute the required Fibonacci number using fast doubling.
</details>
<details>
<summary>Hint 3</summary>
2a (Matrix Exponentiation): Let f[n] count ordered sequences of positive odd integers summing to n. Show that f[1] = f[2] = 1 and f[n] = f[n - 1] + f[n - 2] for n >= 3.
</details>
<details>
<summary>Hint 4</summary>
2b (Matrix Exponentiation): Represent this recurrence with a two-state transition matrix and use binary exponentiation. Multiply the result by the number of choices for the first character.
</details>