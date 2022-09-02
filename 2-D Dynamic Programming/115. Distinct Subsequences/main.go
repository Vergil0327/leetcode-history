// https://leetcode.com/problems/distinct-subsequences/
package main

import "fmt"

/*
Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
*/

// T:O(m*n) M:O(m*n)
// prerequisite: 1143. Longest Common Subsequence
// https://leetcode.com/problems/distinct-subsequences/discuss/1474260/Python-2-approaches%3A-Top-down-DP-Bottom-up-DP-O(N)-Space-Clean-and-Concise
// https://leetcode.com/problems/distinct-subsequences/discuss/37387/A-DP-solution-with-clarification-and-explanation
// https://leetcode.com/problems/distinct-subsequences/discuss/37316/7-10-lines-C%2B%2B-Solutions-with-Detailed-Explanations-(O(m*n)-time-and-O(m)-space)
// https://leetcode.com/problems/distinct-subsequences/discuss/37327/Easy-to-understand-DP-in-Java
func numDistinctBottomUp(s string, t string) int {
	lenS, lenT := len(s), len(t)
	dp := make([][]int, lenS+1)
	for i := range dp {
		dp[i] = make([]int, lenT+1)
	}

	// ! for t as "", s always has 1 distinct (not take s)
	for i := 0; i < lenS+1; i++ {
		dp[i][0] = 1
	}

	for i := 1; i < lenS+1; i++ {
		for j := 1; j < lenT+1; j++ {
			dp[i][j] = dp[i-1][j] // skip s[i]
			if s[i-1] == t[j-1] { // don't skip when characters is equal to each other
				dp[i][j] += dp[i-1][j-1]
			}
		}
	}

	return dp[lenS][lenT]
}

// https://leetcode.com/problems/distinct-subsequences/discuss/1474260/Python-2-approaches%3A-Top-down-DP-Bottom-up-DP-O(N)-Space-Clean-and-Concise
// we can see that we only need previous dp
// T:O(m*n) M:O(n)
func numDistinctSpaceOptimized(s string, t string) int {
	lenS, lenT := len(s), len(t)
	dp := make([]int, lenT+1)
	dpPrev := make([]int, lenT+1)

	// ! for t as "", s always has 1 distinct (not take s)
	dp[0] = 1
	dpPrev[0] = 1

	for i := 1; i < lenS+1; i++ {
		for j := 1; j < lenT+1; j++ {
			dp[j] = dpPrev[j]
			if s[i-1] == t[j-1] {
				dp[j] += dpPrev[j-1]
			}
		}
		dp, dpPrev = dpPrev, dp // dpPrev = dp <--- we need to return dp
	}

	return dpPrev[lenT]
}

// Top-Down Approach
// https://www.youtube.com/watch?v=-RDzMJ33nx8
// https://leetcode.com/problems/distinct-subsequences/discuss/1474260/Python-2-approaches%3A-Top-down-DP-Bottom-up-DP-O(N)-Space-Clean-and-Concise
// T:O(m*n) O:(m*n)
func numDistinctTopDown(s string, t string) int {
	memo := map[string]int{}

	var explore func(lenS, lenT int) int
	explore = func(lenS, lenT int) int {
		if lenT == 0 {
			return 1
		}

		if lenS == 0 {
			return 0
		}

		key := fmt.Sprintf("%d,%d", lenT, lenS)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		count := explore(lenS-1, lenT)
		if s[lenS-1] == t[lenT-1] {
			count += explore(lenS-1, lenT-1)
		}

		memo[key] = count
		return memo[key]
	}

	return explore(len(s), len(t))
}

func numDistinctRuntimeError(s string, t string) int {
	memo := map[string]int{}

	var explore func(str, target string) int
	explore = func(str, target string) int {
		if len(target) == 0 {
			return 1
		}

		if len(str) == 0 {
			return 0
		}

		key := fmt.Sprintf("%s,%s", str, target) // ! OUT OF MEMORY ERROR IF STR IS TOO LONG
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		count1 := explore(str[:len(str)-1], target)
		var count2 int
		if str[len(str)-1] == target[len(target)-1] {
			count2 = explore(str[:len(str)-1], target[:len(target)-1])
		}

		memo[key] = count1 + count2
		return memo[key]
	}

	return explore(s, t)
}

func numDistinctAnotherTimeout(s string, t string) int {
	memo := map[string]int{}

	var dfs func(i int, str string) int
	dfs = func(i int, str string) int {
		if len(str) == 0 {
			return 1
		}

		if i == len(s) {
			return 0
		}

		key := fmt.Sprintf("%d,%s", i, str)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		count1 := dfs(i+1, str)
		var count2 int
		if s[i] == str[0] {
			count2 = dfs(i+1, str[1:])
		}

		memo[key] = count1 + count2
		return memo[key]
	}

	return dfs(0, t)
}

func numDistinctStillTimeout(s string, t string) int {
	var dfs func(i int, str string) int
	dfs = func(i int, str string) int {
		if len(str) > len(t) {
			return 0
		}

		if i == len(s) && str == t {
			return 1
		}

		if i == len(s) {
			return 0
		}

		return dfs(i+1, str) + dfs(i+1, str+string(s[i]))
	}

	return dfs(0, "")
}

// T:O(2^n*m)
func numDistinctTimeout(s string, t string) int {
	state := []string{}
	var dfs func(i int, str string)
	dfs = func(i int, str string) {
		if len(str) > len(t) {
			return
		}

		// comparison of string: T:O(m), m for length of t
		if i == len(s) && str == t {
			state = append(state, str)
			return
		}

		if i == len(s) {
			return
		}

		dfs(i+1, str)
		dfs(i+1, str+string(s[i]))
	}
	dfs(0, "")

	return len(state)
}
