[2514. Count Anagrams](https://leetcode.com/problems/count-anagrams/description/)

`Hard`

You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.

```
Example 1:
Input: s = "too hot"
Output: 18
Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".

Example 2:
Input: s = "aa"
Output: 1
Explanation: There is only one anagram possible for the given string.
```

Constraints:

- 1 <= s.length <= 10^5
- s consists of lowercase English letters and spaces ' '.
- There is single space between consecutive words.

<details>
<summary>Hint 1</summary>

For each word, can you count the number of permutations possible if all characters are distinct?

</details>

<details>
<summary>Hint 2</summary>

How to reduce overcounting when letters are repeated?

</details>

<details>
<summary>Hint 3</summary>

The product of the counts of distinct permutations of all words will give the final answer.

</details>