[1092. Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)

`Hard`

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

```
Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
```

Constraints:

- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of lowercase English letters.


<details>
<summary>Hint 1</summary>

We can find the length of the longest common subsequence between str1[i:] and str2[j:] (for all (i, j)) by using dynamic programming.

</details>

<details>
<summary>Hint 2</summary>

We can use this information to recover the shortest common supersequence.

</details>

<details>
<summary>Video Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=Uk9JRbylA0c&ab_channel=HuifengGuan)
</details>