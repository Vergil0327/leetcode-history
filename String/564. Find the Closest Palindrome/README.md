[564. Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/)

`Hard`

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

```
Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
``` 

Constraints:

0 1 <= n.length <= 18
0 n consists of only digits.
0 n does not have leading zeros.
0 n is representing an integer in the range [1, 10^18 - 1].

Accepted
41.3K
Submissions
188.9K
Acceptance Rate
21.9%

<details>
<summary>Hint 1</summary>

Will brute force work for this problem? Think of something else.

</details>
<details>
<summary>Hint 2</summary>

Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?

</details>
<details>
<summary>Hint 3</summary>

Do we have to consider only left half or right half of the string or both?

</details>
<details>
<summary>Hint 4</summary>

Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?

</details>