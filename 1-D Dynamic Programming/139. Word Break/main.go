// https://leetcode.com/problems/word-break/
package main

import "strings"

/*
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

constraints:
	- 1 <= s.length <= 300
	- 1 <= wordDict.length <= 1000
	- 1 <= wordDict[i].length <= 20
	- s and wordDict[i] consist of only lowercase English letters.
	- All the strings of wordDict are unique.
*/

// "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
// ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
// Expected: false

// explanation: https://www.youtube.com/watch?v=Sx9NNgInc3A
func wordBreakDP(s string, wordDict []string) bool {
	dp := make([]bool, len(s)+1)
	dp[len(s)] = true

	for i := len(s) - 1; i >= 0; i-- {
		for _, w := range wordDict {
			if i+len(w) <= len(s) && s[i:i+len(w)] == w {
				dp[i] = dp[i+len(w)]
			}
			if dp[i] {
				break
			}
		}
	}

	return dp[0]
}

func wordBreak3(s string, wordDict []string) bool {
	memo := map[int]bool{}

	var dfs func(i int, memo map[int]bool) bool
	dfs = func(i int, memo map[int]bool) bool {
		if memo[i] {
			return false
		}

		if i == len(s) {
			return true
		}

		for _, word := range wordDict {
			if strings.HasPrefix(s[i:], word) {
				if dfs(i+len(word), memo) {
					return true
				}
			}
		}

		memo[i] = true
		return false
	}

	return dfs(0, memo)
}

func wordBreak2(s string, wordDict []string) bool {
	memo := map[string]bool{}

	var dfs func(i int, memo map[string]bool) bool
	dfs = func(i int, memo map[string]bool) bool {
		if memo[s[i:]] {
			return false
		}

		if i == len(s) {
			return true
		}

		for _, word := range wordDict {
			if strings.HasPrefix(s[i:], word) {
				if dfs(i+len(word), memo) {
					return true
				}
			}
		}

		memo[s[i:]] = true
		return false
	}

	return dfs(0, memo)
}

// brute force: T:O(n*m * n), n for length of s & m for length of wordDict
func wordBreak1(s string, wordDict []string) bool {
	memo := map[string]bool{}

	var dfs func(str string, memo map[string]bool) bool
	dfs = func(str string, memo map[string]bool) bool {
		if memo[str] {
			return false
		}

		if str == "" {
			return true
		}

		for _, word := range wordDict {
			// HasPrefix: T:O(n)
			if strings.HasPrefix(str, word) {
				if dfs(str[len(word):], memo) {
					return true
				}
			}
		}

		memo[str] = true
		return false
	}

	return dfs(s, memo)
}
