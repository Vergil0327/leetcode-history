// https://leetcode.com/problems/palindromic-substrings/
package main

/*
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
*/

// explanation: https://www.youtube.com/watch?v=4RACzI5-du8
func countSubstrings(s string) int {
	count := 0

	for i := range s {
		// odd
		l, r := i, i
		for l >= 0 && r < len(s) && s[l] == s[r] {
			count += 1

			l, r = l-1, r+1
		}

		// even
		l, r = i, i+1
		for l >= 0 && r < len(s) && s[l] == s[r] {
			count += 1

			l, r = l-1, r+1
		}
	}

	return count
}

// discussion: https://leetcode.com/problems/palindromic-substrings/discuss/105707/Java-Python-DP-solution-based-on-longest-palindromic-substring
func countSubstringsDP(s string) int {
	count := 0

	// dp[i][j] means s[i:j+1]
	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
		dp[i][i] = true
	}

	for start := len(s) - 1; start >= 0; start-- {
		for end := start; end < len(s); end++ {
			if s[start] == s[end] /* character match */ {
				// ! wrong order
				// if dp[start+1][end-1] || end-start+1 < 3 {
				// 	dp[start][end] = true
				// 	count += 1
				// }

				// check substring length first, then check dp table
				// if end-start+1 == 1, ex. A, must be valid palindrom
				// if end-start+1 == 2, ex. AA, must be valid palindrom
				// if end-start+1 == 3, ex. AXA, must be valid palindrom
				if end-start+1 <= 3 || dp[start+1][end-1] {
					dp[start][end] = true
					count += 1
				}
			}
		}
	}

	return count
}
