// https://leetcode.com/problems/regular-expression-matching/

package main

import "fmt"

/*
Intuition: compare s[i:] with p[j:] (prefix)
we solve from end to start position.

base case we check:
	- s: "", p:""
	- s: "...", p:""
	- s: "", p:"..."
we can compare len-1 and use len-2 to get what comes before special character '.' & '*',
and don't forget we have choice to not use '*' because '*' matches ZERO or more
*/

// Time Complexity: Let T, P be the lengths of the text and the pattern respectively
// The work for every call to dp(i, j) for lenS=T,...,0; j=P,...,0 is done once, and it is O(1) work.
// T:O(m*n)
func isMatchMemo(s string, p string) bool {
	memo := map[string]bool{}

	var dfs func(lenS, lenP int) bool
	dfs = func(lenS, lenP int) bool {
		key := fmt.Sprintf("%d,%d", lenS, lenP)

		if lenS == 0 && lenP == 0 {
			return true
		}

		if lenS == 0 {
			if c := p[lenP-1]; c == '*' {
				memo[key] = dfs(lenS, lenP-2)
				return memo[key]
			} else if c == '.' {
				return false
			} else {
				return false
			}
		}

		if lenP == 0 {
			return false
		}

		if _, ok := memo[key]; ok {
			return memo[key]
		}

		if s[lenS-1] == p[lenP-1] {
			memo[key] = dfs(lenS-1, lenP-1)
			return memo[key]
		} else {
			if c := p[lenP-1]; c == '*' {
				prev := p[lenP-2]
				if prev == '.' || prev == s[lenS-1] {
					memo[key] = dfs(lenS-1, lenP) || dfs(lenS, lenP-2)
					return memo[key]
				} else {
					memo[key] = dfs(lenS, lenP-2)
					return memo[key]
				}
			} else if c == '.' {
				memo[key] = dfs(lenS-1, lenP-1)
				return memo[key]
			} else {
				memo[key] = false
				return memo[key]
			}
		}
	}

	return dfs(len(s), len(p))
}

func isMatch(s string, p string) bool {
	var dfs func(lenS, lenP int) bool
	dfs = func(lenS, lenP int) bool {
		if lenS == 0 && lenP == 0 {
			return true
		}

		if lenS == 0 {
			if c := p[lenP-1]; c == '*' {
				return dfs(lenS, lenP-2)
			} else if c == '.' {
				return false
			} else {
				return false
			}
		}

		if lenP == 0 {
			return false
		}

		if s[lenS-1] == p[lenP-1] {
			return dfs(lenS-1, lenP-1)
		} else {
			if c := p[lenP-1]; c == '*' {
				prev := p[lenP-2]
				if prev == '.' || prev == s[lenS-1] {
					return dfs(lenS-1, lenP) || dfs(lenS, lenP-2)
				} else {
					return dfs(lenS, lenP-2)
				}
			} else if c == '.' {
				return dfs(lenS-1, lenP-1)
			} else {
				return false
			}
		}
	}

	return dfs(len(s), len(p))
}
