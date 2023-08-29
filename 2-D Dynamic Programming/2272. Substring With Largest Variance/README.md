[2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/description/)

`Hard`

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

```
Example 1:
Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

Example 2:
Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.
``` 

Constraints:

- 1 <= s.length <= 10^4
- s consists of lowercase English letters.

Acceptance Rate
40.8%

<details>
<summary>Hint 1</summary>

Think about how to solve the problem if the string had only two distinct characters.

</details>

<details>
<summary>Hint 2</summary>

If we replace all occurrences of the first character by +1 and those of the second character by -1, can we efficiently calculate the largest possible variance of a string with only two distinct characters?

</details>

<details>
<summary>Hint 3</summary>

Now, try finding the optimal answer by taking all possible pairs of characters into consideration.

</details>

<details>
<summary>Video Explanation on Youtube</summary>

[HuifengGuan](https://www.youtube.com/watch?v=P6KnO-Dw0Fo)
</details>