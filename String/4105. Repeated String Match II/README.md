[4105. Repeated String Match II](https://leetcode.com/problems/repeated-string-match-ii/)

`Hard`

You are given two strings a and b​​​​​​​ consisting of lowercase English letters, and two integers x and y.

Return true if the string formed by repeating b exactly y times (b * y) is a substring of the string formed by repeating a exactly x times (a * x). Otherwise, return false.

A substring is a contiguous non-empty sequence of characters within a string.
 

Example 1:
Input: a = "ab", b = "abab", x = 2, y = 1
Output: true
Explanation:

a * x = "ab" * 2 = "abab"
b * y = "abab" * 1 = "abab"
They are identical, so b * y is a substring of a * x. Thus, the answer is true.

Example 2:
Input: a = "abc", b = "bc", x = 2, y = 3
Output: false
Explanation:

a * x = "abc" * 2 = "abcabc"
b * y = "bc" * 3 = "bcbcbc"
The answer is false as b * y = "bcbcbc" is not a substring of a * x = "abcabc".

Example 3:
Input: a = "abcd", b = "cdab", x = 2, y = 1
Output: true
Explanation:

a * x = "abcd" * 2 = "abcdabcd"
b * y = "cdab" appears in a * x = "abcdabcd" at indices [2..5]. Thus, the answer is true.
 

Constraints:

- 1 <= a.length <= 100
- 1 <= b.length <= 100
- 1 <= x <= 10^9
- 1 <= y <= 10^9​​​​​​​
- a and b consist of lowercase English letters.

Accepted
2,428/8.1K
Acceptance Rate
30.0%