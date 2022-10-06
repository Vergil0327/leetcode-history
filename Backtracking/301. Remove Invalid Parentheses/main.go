package main

import (
	"math"
	"strings"
)

// T:O(2^n), stil 2^n in worst case. ex. '((((('
func removeInvalidParentheses(s string) []string {
	invalidOpenN, invalidCloseN := checkParen(s)

	res := map[string]struct{}{}

	var dfs func(state []string, i, openN, closeN, invalidOpenN, invalidCloseN int)
	dfs = func(state []string, i, openN, closeN, invalidOpenN, invalidCloseN int) {
		// base case
		if i == len(s) {
			if invalidOpenN == 0 && invalidCloseN == 0 {
				res[strings.Join(state, "")] = struct{}{}
			}

			return
		}

		ch := s[i]

		// keep character other than '(' or ')'
		if ch != '(' && ch != ')' {
			state = append(state, string(ch))
			dfs(state, i+1, openN, closeN, invalidOpenN, invalidCloseN)
			state = state[:len(state)-1]
			return
		}

		if ch == '(' {
			// remove
			if invalidOpenN > 0 {
				dfs(state, i+1, openN, closeN, invalidOpenN-1, invalidCloseN)
			}

			// keep
			state = append(state, string(ch))
			dfs(state, i+1, openN+1, closeN, invalidOpenN, invalidCloseN)
			state = state[:len(state)-1]
		}

		if ch == ')' {
			// remove
			if invalidCloseN > 0 {
				dfs(state, i+1, openN, closeN, invalidOpenN, invalidCloseN-1)
			}

			// keep
			state = append(state, string(ch))
			if closeN < openN {
				dfs(state, i+1, openN, closeN+1, invalidOpenN, invalidCloseN)
			}
			state = state[:len(state)-1]
		}
	}
	dfs([]string{}, 0, 0, 0, invalidOpenN, invalidCloseN)

	ans := []string{}
	for rslt := range res {
		ans = append(ans, rslt)
	}

	return ans
}

// return invalid number of (openN, closeN)
func checkParen(s string) (openN int, closeN int) {
	for _, c := range s {
		if c == '(' {
			openN += 1
		}
		if c == ')' {
			// found invalid close paren
			if openN == 0 {
				closeN += 1
			} else if openN > 0 { // find counter-part
				openN -= 1
			}
		}
	}

	return
}

// Brute Force
// T:O(2^n), we can choose keep or remove at each character
func removeInvalidParenthesesBruteForce(s string) []string {
	res := map[string]struct{}{}
	minRemoved := math.MaxInt

	var dfs func(state []string, idx, openN, closeN, deleted int)
	dfs = func(state []string, idx, openN, closeN, deleted int) {
		// reach the end of string
		if idx == len(s) && openN == closeN {
			// since we only want minimum number of removed parentheses
			// update minRemoved and answer
			if deleted <= minRemoved {
				if deleted < minRemoved {
					minRemoved = deleted
					res = make(map[string]struct{})
				}

				res[strings.Join(state, "")] = struct{}{}
			}

			return
		}

		if idx == len(s) {
			return
		}

		ch := s[idx]

		// simply add character to result
		if ch != '(' && ch != ')' {
			state = append(state, string(ch))
			dfs(state, idx+1, openN, closeN, deleted)
			state = state[:len(state)-1] // backtracking
		} else {
			// 1. remove current character
			dfs(state, idx+1, openN, closeN, deleted+1)

			// 2. keep current if operation is valid
			state = append(state, string(ch))
			if ch == '(' {
				dfs(state, idx+1, openN+1, closeN, deleted)
			} else if closeN < openN { // close parentheses only valid when open paren exists
				dfs(state, idx+1, openN, closeN+1, deleted)
			}
			state = state[:len(state)-1]
		}
	}
	dfs([]string{}, 0, 0, 0, 0)

	ans := []string{}
	for rslt := range res {
		ans = append(ans, rslt)
	}
	return ans
}
