[3579. Minimum Steps to Convert String with Operations](https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/)

`Hard`

You are given two strings, word1 and word2, of equal length. You need to transform word1 into word2.

For this, divide word1 into one or more contiguous substrings. For each substring substr you can perform the following operations:

Replace: Replace the character at any one index of substr with another lowercase English letter.

Swap: Swap any two characters in substr.

Reverse Substring: Reverse substr.

Each of these counts as one operation and each character of each substring can be used in each type of operation at most once (i.e. no single index may be involved in more than one replace, one swap, or one reverse).

Return the minimum number of operations required to transform word1 into word2.
 
```
Example 1:
Input: word1 = "abcdf", word2 = "dacbe"
Output: 4
Explanation:
Divide word1 into "ab", "c", and "df". The operations are:

For the substring "ab",
Perform operation of type 3 on "ab" -> "ba".
Perform operation of type 1 on "ba" -> "da".
For the substring "c" do no operations.
For the substring "df",
Perform operation of type 1 on "df" -> "bf".
Perform operation of type 1 on "bf" -> "be".

Example 2:
Input: word1 = "abceded", word2 = "baecfef"
Output: 4
Explanation:
Divide word1 into "ab", "ce", and "ded". The operations are:

For the substring "ab",
Perform operation of type 2 on "ab" -> "ba".
For the substring "ce",
Perform operation of type 2 on "ce" -> "ec".
For the substring "ded",
Perform operation of type 1 on "ded" -> "fed".
Perform operation of type 1 on "fed" -> "fef".

Example 3:
Input: word1 = "abcdef", word2 = "fedabc"
Output: 2
Explanation:
Divide word1 into "abcdef". The operations are:

For the substring "abcdef",
Perform operation of type 3 on "abcdef" -> "fedcba".
Perform operation of type 2 on "fedcba" -> "fedabc".
```

Constraints:

- 1 <= word1.length == word2.length <= 100
- word1 and word2 consist only of lowercase English letters.

Accepted
1,836/5.6K
Acceptance Rate
32.9%

<details>
<summary>Hint 1</summary>

Use dynamic programming

</details>
<details>
<summary>Hint 2</summary>

Do DP on disjoint substrings of word1. For the DP, we try both the substring and its reversed version (just add one extra operation)

</details>
<details>
<summary>Hint 3</summary>

First we swap pairs like (word1[i], word2[i]) and (word1[j], word2[j]) where word1[i] == word2[j] and word2[i] == word1[j]

</details>
<details>
<summary>Hint 4</summary>

For the remaining characters, we use replace operations

</details>