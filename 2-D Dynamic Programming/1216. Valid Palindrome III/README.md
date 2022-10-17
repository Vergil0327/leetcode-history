[1216. Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/)

*SUBSCRIBE TO UNLOCK*

Description:

Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length

<details>
<summary>Solution</summary>

[bottom-up](https://www.cnblogs.com/Dylan-Java-NYC/p/12028253.html)
[top-down](https://github.com/awangdev/leet-code/blob/master/Java/1216.%20Valid%20Palindrome%20III.java)
</details>

```go
func isValidPalindrome(s string, k int) bool {
  var dfs func(l, r, k int) bool
  dfs = func(l, r, k int) bool {
    if l == r {
      return true
    }

    if s[l] == s[r] {
      return dfs(l+1, r-1, k)
    } else {
      return dfs(l+1, r, k-1) || dfs(l, r-1, k-1)
    }
  }

  return dfs(0, len(s)-1, k)
}
```