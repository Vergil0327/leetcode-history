// https://leetcode.com/problems/longest-palindromic-substring/
package main

/*
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
*/

// T:O(n^2)
func longestPalindromeBetter(s string) string {
	longest := ""
	length := 0

	for i := range s {
		// odd length
		l, r := i, i
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if r-l+1 > length {
				length = r - l + 1
				longest = s[l : r+1]
			}

			l, r = l-1, r+1
		}

		// even length
		l, r = i, i+1
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if r-l+1 > length {
				length = r - l + 1
				longest = s[l : r+1]
			}
			l, r = l-1, r+1
		}
	}

	return longest
}

// https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP
// T:O(n^2) M:O(n^2)
func longestPalindromeDP(s string) string {
	longest := ""
	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
		dp[i][i] = true // filling out the diagonal by true because s[i:i+1] is always a palindrom
		longest = string(s[i])
	}

	for start := len(s) - 1; start >= 0; start-- {
		for end := start + 1; end < len(s); end++ {
			if s[start] == s[end] /* if the chars mathces */ {
				// if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
				if end-start == 1 || dp[start+1][end-1] {
					dp[start][end] = true

					// update result
					if end-start+1 > len(longest) {
						longest = s[start : end+1]
					}
				}
			}
		}
	}

	return longest
}

// T:O(n^2*n)
func longestPalindromeSlow(s string) string {
	if len(s) == 1 {
		return s
	}

	longest := ""
	for i := 0; i < len(s); i++ {
		for j := i; j < len(s); j++ {
			if isPalindrom(s[i : j+1]) {
				if j-i+1 > len(longest) {
					longest = s[i : j+1]
				}
			}
		}
	}
	return longest
}

func isPalindrom(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l, r = l+1, r-1
	}
	return true
}
