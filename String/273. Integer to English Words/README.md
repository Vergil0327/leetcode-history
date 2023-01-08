[273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/description/)

`Hard`

Convert a non-negative integer num to its English words representation.

```
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

Constraints:

- 0 <= num <= 2^31 - 1

<details>
<summary>Hint 1</summary>

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.

</details>

<details>
<summary>Hint 2</summary>

Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.

</details>

<details>
<summary>Hint 3</summary>

There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

</details>