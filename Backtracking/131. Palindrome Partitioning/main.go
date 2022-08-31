// https://leetcode.com/problems/palindrome-partitioning/
package main

/*
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]] */

// explanation: https://www.youtube.com/watch?v=3jvWodd7ht0
func partition(s string) [][]string {
	solutions := [][]string{}

	var dfs func(state []string, idx int)
	dfs = func(state []string, idx int) {
		// pass through checkPalindrome fn
		if idx >= len(s) {
			cpy := make([]string, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		for j := idx; j < len(s); j++ {
			if checkPalindrome(s, idx, j) /* means s[i:j+1] is palindrome */ {
				state = append(state, s[idx:j+1])
				dfs(state, j+1) // find substring from next character
				state = state[:len(state)-1]
			}
		}
	}

	dfs([]string{}, 0)
	return solutions
}

func checkPalindrome(s string, l, r int) bool {
	for l < r {
		if s[l] != s[r] {
			return false
		}

		l += 1
		r -= 1
	}
	return true
}
