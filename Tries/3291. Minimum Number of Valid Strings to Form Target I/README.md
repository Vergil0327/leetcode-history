[3291. Minimum Number of Valid Strings to Form Target I](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/)

`Medium`

You are given an array of strings words and a string target.

A string x is called valid if x is a 
prefix
 of any string in words.

Return the minimum number of valid strings that can be concatenated to form target. If it is not possible to form target, return -1.

```
Example 1:
Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
Output: 3
Explanation:
The target string can be formed by concatenating:
Prefix of length 2 of words[1], i.e. "aa".
Prefix of length 3 of words[2], i.e. "bcd".
Prefix of length 3 of words[0], i.e. "abc".

Example 2:
Input: words = ["abababab","ab"], target = "ababaababa"
Output: 2
Explanation:
The target string can be formed by concatenating:
Prefix of length 5 of words[0], i.e. "ababa".
Prefix of length 5 of words[0], i.e. "ababa".

Example 3:
Input: words = ["abcdef"], target = "xyz"
Output: -1
```

Constraints:

- 1 <= words.length <= 100
- 1 <= words[i].length <= 5 * 10^3
- The input is generated such that sum(words[i].length) <= 10^5.
- words[i] consists only of lowercase English letters.
- 1 <= target.length <= 5 * 10^3
- target consists only of lowercase English letters.

Accepted
8.8K
Submissions
50.3K
Acceptance Rate
17.5%

<details>
<summary>Hint 1</summary>

Let dp[i] be the minimum cost to form the prefix of length i of target.

</details>
<details>
<summary>Hint 2</summary>

If target[(i + 1)..j] matches any prefix, update the range dp[(i + 1)..j] to minimum between original value and dp[i] + 1.

</details>
<details>
<summary>Hint 3</summary>

Use a Trie to check prefix matching.

</details>