// https://leetcode.com/problems/valid-parenthesis-string/
package main

import "fmt"

/*
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
*/

// true, "()"
// true, "()()"
// true, "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
// false,"(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)"
// false,"(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

// Greedy: T:O(n) M:O(1)
func checkValidString(s string) bool {
	leftMin, leftMax := 0, 0 // respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.
	for _, ch := range s {
		if ch == '(' {
			leftMin, leftMax = leftMin+1, leftMax+1
		}
		if ch == ')' {
			leftMin, leftMax = leftMin-1, leftMax-1
		}
		if ch == '*' {
			leftMin -= 1 // AS )
			leftMax += 1 // AS (
		}

		if leftMax < 0 {
			return false
		}
		if leftMin < 0 { // without statement, it won't pass. take this as example: (*)(
			leftMin = 0 // we can never have less than 0 open left brackets
		}
	}

	return leftMin == 0 // if greater than 0, means invalid
}

// T:O(3^n), 3 for asterisk's three possibility branch and n for length of string (height of tree)
func checkValidStringBruteForce(s string) bool {
	var dfs func(i int, leftParan int) bool
	dfs = func(i, leftParan int) bool {
		if leftParan < 0 {
			return false
		}

		if i == len(s) {
			return leftParan == 0
		}

		if s[i] == '(' {
			return dfs(i+1, leftParan+1)
		}
		if s[i] == ')' {
			return dfs(i+1, leftParan-1)
		}
		if s[i] == '*' {
			return dfs(i+1, leftParan) || // AS ""
				dfs(i+1, leftParan+1) || // AS (
				dfs(i+1, leftParan-1) // AS )
		}

		return leftParan == 0
	}

	return dfs(0, 0)
}

// T:O(n^2*n)
// cache i & leftParan -> 2-D cache and calculate each value in matrix cost O(n)
func checkValidStringDFS_MEMO(s string) bool {
	memo := map[string]bool{}

	var dfs func(i int, leftParan int, memo map[string]bool) bool
	dfs = func(i, leftParan int, memo map[string]bool) bool {
		if leftParan < 0 {
			return false
		}

		if i == len(s) {
			return leftParan == 0
		}

		key := fmt.Sprintf("%d,%d", i, leftParan)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		if s[i] == '(' {
			memo[key] = dfs(i+1, leftParan+1, memo)
		}
		if s[i] == ')' {
			memo[key] = dfs(i+1, leftParan-1, memo)
		}
		if s[i] == '*' {
			memo[key] = dfs(i+1, leftParan, memo) || // AS ""
				dfs(i+1, leftParan+1, memo) || // AS (
				dfs(i+1, leftParan-1, memo) // AS )
		}

		return memo[key]
	}

	return dfs(0, 0, memo)
}
