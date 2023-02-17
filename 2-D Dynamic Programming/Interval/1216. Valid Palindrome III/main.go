package main

import "fmt"

func isValidPalindrome(s string, k int) bool {
	memo := map[string]bool{}

	var dfs func(l, r, k int) bool
	dfs = func(l, r, k int) bool {
		if l == r {
			return k >= 0
		}

		if k < 0 {
			return false
		}

		key := fmt.Sprintf("%d,%d,%d", l, r, k)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		if s[l] == s[r] {
			memo[key] = dfs(l+1, r-1, k)
			return memo[key]
		} else {
			memo[key] = dfs(l+1, r, k-1) || dfs(l, r-1, k-1)
			return memo[key]
		}
	}

	return dfs(0, len(s)-1, k)
}

func isValidPalindromeBottomUp(s string, k int) bool {
	dp := make([][]int, len(s))
	for i := range dp {
		dp[i] = make([]int, len(s))
	}

	// find every possible palindrome's length
	// we check if there is a palindrome those length is less than or equal to k
	for l := len(s) - 1; l >= 0; l-- {
		// base case:
		dp[l][l] = 1
		for r := l + 1; r < len(s); r++ {
			if s[l] == s[r] {
				dp[l][r] = dp[l+1][r-1] + 2
			} else {
				dp[l][r] = max(dp[l+1][r], dp[l][r-1])
			}
		}
	}

	maxPalindromeLen := dp[0][len(s)-1]
	return abs(maxPalindromeLen-len(s)) <= k
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func abs(num int) int {
	if num < 0 {
		return -num
	}

	return num
}
