// https://leetcode.com/problems/generate-parentheses/
package main

import (
	"strings"
)

// https://www.youtube.com/watch?v=s9fokUqJ76A
// only add open parenthesis if open < n
// only add a closing parenthesis if closed < open
// valid IF open == closed == n
func generateParenthesis(n int) []string {
	result := []string{}
	stack := []string{}

	var backtracking func(openN, closeN int)
	backtracking = func(openN, closeN int) {
		// base case
		if openN == closeN && closeN == n {
			result = append(result, strings.Join(stack, ""))
		}

		if openN < n {
			stack = append(stack, "(")
			backtracking(openN+1, closeN)
			stack = stack[:len(stack)-1] // ! clean global stack
		}

		if closeN < openN {
			stack = append(stack, ")")
			backtracking(openN, closeN+1)
			stack = stack[:len(stack)-1] // ! clean global stack
		}
	}
	backtracking(0, 0)

	return result
}

// move backtracking out of generateParenthesis

func generateParenthesis2(n int) []string {
	result := []string{}
	stack := []string{}

	backtracking2(0, 0, n, stack, &result)

	return result
}

func backtracking2(openN, closeN, n int, stack []string, result *[]string) {
	// base case
	if openN == closeN && closeN == n {
		*result = append(*result, strings.Join(stack, ""))
		stack = stack[:len(stack)-1]
	}

	if openN < n {
		stack = append(stack, "(")
		backtracking2(openN+1, closeN, n, stack, result)
		stack = stack[:len(stack)-1] // ! clean global stack
	}

	if closeN < openN {
		stack = append(stack, ")")
		backtracking2(openN, closeN+1, n, stack, result)
		stack = stack[:len(stack)-1] // ! clean global stack
	}
}
