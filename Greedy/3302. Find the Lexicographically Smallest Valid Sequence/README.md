[3302. Find the Lexicographically Smallest Valid Sequence](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/)

`Medium`

You are given two strings word1 and word2.

A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

A sequence of indices seq is called valid if:

The indices are sorted in ascending order.
Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
Return an array of size word2.length representing the 
lexicographically smallest
 valid sequence of indices. If no such sequence of indices exists, return an empty array.

Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

```
Example 1:
Input: word1 = "vbcca", word2 = "abc"
Output: [0,1,2]
Explanation:
The lexicographically smallest valid sequence of indices is [0, 1, 2]:
Change word1[0] to 'a'.
word1[1] is already 'b'.
word1[2] is already 'c'.

Example 2:
Input: word1 = "bacdc", word2 = "abc"
Output: [1,2,4]
Explanation:
The lexicographically smallest valid sequence of indices is [1, 2, 4]:
word1[1] is already 'a'.
Change word1[2] to 'b'.
word1[4] is already 'c'.

Example 3:
Input: word1 = "aaaaaa", word2 = "aaabc"
Output: []
Explanation:
There is no valid sequence of indices.

Example 4:
Input: word1 = "abc", word2 = "ab"
Output: [0,1]
```

Constraints:

- 1 <= word2.length < word1.length <= 3 * 10^5
- word1 and word2 consist only of lowercase English letters.

Accepted
2.7K
Submissions
21.2K
Acceptance Rate
12.9%

<details>
<summary>Hint 1</summary>

Let dp[i] be the longest suffix of word2 that exists as a subsequence of suffix of the substring of word1 starting at index i.

</details>
<details>
<summary>Hint 2</summary>

If dp[i + 1] < m and word1[i] == word2[m - dp[i + 1] - 1],dp[i] =  dp[i + 1] + 1. Otherwise, dp[i] =  dp[i + 1].

</details>
<details>
<summary>Hint 3</summary>

For each index i, greedily select characters using the dp array to know whether a solution exists.

</details>