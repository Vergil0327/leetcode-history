package main

// aaabaab, a
// aabaab, aab
// ""

// abcabcdabc, abc
// abcdabc, ""
// ""
// aaabaab, a
// aabaab, aab
// ""

// abcabcdabc, abc
// abcdabc, ""
// ""

// https://leetcode.com/problems/maximum-deletions-on-a-string/discuss/2648900/JavaC%2B%2BPython-DP-Solution
// Explanation:

// lcs[i][j] means the length of the longest common substring.
// If lcs[i][j] = k,
// then s.substring(i, i + k) == s.substring(j, j + k)
// and s.substring(i, i + k + 1) != s.substring(j, j + k + 1).
// This can be done in O(n^2).

// dp[i] mean the the maximum number of operations to delete
// the substring starting at s[i].

// If lcs[i][j] >= j - i,
// s.substring(i, j) == s.substring(j, j + j - i)
// this means we can delete the prefix s.substring(i, j) from s.substring(i),
// and it changes to s.substring(j).
// And we update dp[i] = max(dp[i], dp[j] + 1)
func deleteString(s string) int {
	set := map[byte]bool{}
	for i := 0; i < len(s); i++ {
		set[s[i]] = true
	}
	if len(set) == 1 {
		return len(s)
	}

	LCS := make([][]int, len(s)+1)
	for i := range LCS {
		LCS[i] = make([]int, len(s)+1)
	}

	dp := make([]int, len(s))
	for i := range dp {
		dp[i] = 1 // one delete operation at least
	}

	for i := len(s) - 1; i >= 0; i-- {
		for j := i + 1; j < len(s); j++ {
			if s[i] == s[j] {
				LCS[i][j] = LCS[i+1][j+1] + 1
			}

			// LCS length between s[i:i+k] and s[j:j+k]
			// => s[i:j] can be deleted
			if LCS[i][j] >= j-i {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
	}

	return dp[0]
}

// T:O(n^3)
func deleteStringTopDown(s string) int {
	memo := map[int]int{}

	var dfs func(i int) int
	dfs = func(i int) int {
		if i >= len(s) {
			return 0
		}

		if _, ok := memo[i]; ok {
			return memo[i]
		}

		// !!! important, base case, every position can do 1 deletion at least
		memo[i] = 1

		for j := 1; j <= (len(s)-i)/2; j++ {
			pattern := s[i : i+j]
			target := s[i+j : i+j+len(pattern)]
			if pattern == target {
				memo[i] = max(memo[i], 1+dfs(i+j))
			}
		}

		return memo[i]
	}

	return dfs(0)
}

// Top-Down
// https://leetcode.com/problems/maximum-deletions-on-a-string/discuss/2648927/DP-%2B-LPS
func deleteStringBruteForce(s string) int {
	dp := make([]int, 40000) // constraint: 1 <= s.length <= 4000

	var dfs func(i int) int
	dfs = func(i int) int {
		if dp[i] == 0 {
			dp[i] = 1 // if we can't delete substring, we can delete all. thus, 1 operation at least

			// try all possibilities
			for length := 1; length <= (len(s)-i)/2; length++ {
				pattern := s[i : i+length]
				target := s[i+length : i+length+len(pattern)]
				if target == pattern {
					dp[i] = max(dp[i], 1+dfs(i+length)) // try remaining string
				}
			}
		}

		return dp[i]
	}

	return dfs(0)
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
