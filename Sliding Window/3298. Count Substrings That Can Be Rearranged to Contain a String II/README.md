[3298. Count Substrings That Can Be Rearranged to Contain a String II](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)

`Hard`

You are given two strings word1 and word2.

A string x is called valid if x can be rearranged to have word2 as a prefix.

Return the total number of valid 
substrings
 of word1.

Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.

```
Example 1:
Input: word1 = "bcca", word2 = "abc"
Output: 1
Explanation:
The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.

Example 2:
Input: word1 = "abcabc", word2 = "abc"
Output: 10
Explanation:
All the substrings except substrings of size 1 and size 2 are valid.

Example 3:
Input: word1 = "abcabc", word2 = "aaabc"
Output: 0
```

Constraints:

- 1 <= word1.length <= 10^5
- 1 <= word2.length <= 10^4
- word1 and word2 consist only of lowercase English letters.

Accepted
10.5K
Submissions
17.6K
Acceptance Rate
59.3%

<details>
<summary>Hint 1</summary>

Use sliding window along with two-pointer here.

</details>
<details>
<summary>Hint 2</summary>

Use constant space to store the frequency of characters.

</details>