[1839. Longest Substring Of All Vowels in Order](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/)
`Medium`


A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

```
Example 1:
Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.

Example 2:
Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.

Example 3:
Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
```

Constraints:

- 1 <= word.length <= 5 * $10^5$
- word consists of characters 'a', 'e', 'i', 'o', and 'u'.

<details>
<summary>Hint 1</summary>

Start from each 'a' and find the longest beautiful substring starting at that index.

</details>

<details>
<summary>Hint 2</summary>

Based on the current character decide if you should include the next character in the beautiful substring.

</details>

also other solution here:

[greedy](../../Greedy/1839.%20Longest%20Substring%20Of%20All%20Vowels%20in%20Order/)