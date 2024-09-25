[3292. Minimum Number of Valid Strings to Form Target II](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/)

`Hard`

You are given an array of strings words and a string target.

A string x is called valid if x is a prefix of any string in words.

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
- 1 <= words[i].length <= 5 * 10^4
- The input is generated such that sum(words[i].length) <= 105.
- words[i] consists only of lowercase English letters.
- 1 <= target.length <= 5 * 10^4
- target consists only of lowercase English letters.

Accepted
2.8K
Submissions
18.4K
Acceptance Rate
15.4%

<details>
<summary>Hint 1</summary>

Let dp[i] be the minimum cost to form the prefix of length i of target.

</details>
<details>
<summary>Hint 2</summary>

Use Rabin-Karp to hash every prefix and store it in a HashSet.

</details>
<details>
<summary>Hint 3</summary>

Use Binary search to find the longest substring starting at index i (target[i..j]) that has a hash present in the HashSet.

</details>
<details>
<summary>Hint 4</summary>

Inverse Modulo precomputation can optimise hash calculation.

</details>
<details>
<summary>Hint 5</summary>

Use Lazy Segment Tree, or basic Segment Tree to update dp[i..j].

</details>
<details>
<summary>Hint 6</summary>

Is it possible to use two TreeSets to update dp[i..j]?

</details>