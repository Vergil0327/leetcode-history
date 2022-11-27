[2484. Count Palindromic Subsequences](https://leetcode.com/problems/count-palindromic-subsequences/)

`Hard`

Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.

Note:

A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 
```
Example 1:
Input: s = "103301"
Output: 2
Explanation: 
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
Two of them (both equal to "10301") are palindromic.

Example 2:
Input: s = "0000000"
Output: 21
Explanation: All 21 subsequences are "00000", which is palindromic.

Example 3:
Input: s = "9999900000"
Output: 2
Explanation: The only two palindromic subsequences are "99999" and "00000".
```

Constraints:

- 1 <= s.length <= 10^4
- s consists of digits.

<details>
<summary>Hint 1</summary>

There are 100 possibilities for the first two characters of the palindrome.
</details>

<details>
<summary>Hint 2</summary>

Iterate over all characters, letting the current character be the center of the palindrome.
</details>

<details>
<summary>Solution</summary>

[100N solution - prefix & suffix sum](https://leetcode.com/problems/count-palindromic-subsequences/discuss/2850466/C%2B%2B-Java-Python3-Counting-Prefixes-and-Suffixes)

[100N solution - pattern](https://leetcode.com/problems/count-palindromic-subsequences/discuss/2850557/C%2B%2BorJavaorPython3-short-DP): same idea as 4 hashmap
</details>