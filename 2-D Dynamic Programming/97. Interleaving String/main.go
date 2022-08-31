// https://leetcode.com/problems/interleaving-string/
package main

import "fmt"

/*
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

*/

// explanation: https://www.youtube.com/watch?v=3Rw3p9LrgvE
// other explanation: https://www.youtube.com/watch?v=XaFwHqyYde0
func isInterleaveDP(s1 string, s2 string, s3 string) bool {
	if len(s3) != len(s1)+len(s2) {
		return false
	}

	dp := make([][]bool, len(s1)+1)
	for i := 0; i < len(s1)+1; i++ {
		dp[i] = make([]bool, len(s2)+1)
	}
	dp[len(s1)][len(s2)] = true // means if letter at (i+j) in s3 which is empty string("") can be composed of "" from s1 and "" from s2 => YES

	// from bottom-right to top-left
	for i := len(s1); i >= 0; i-- {
		for j := len(s2); j >= 0; j-- {
			// similar logic in DFS
			if i < len(s1) && s1[i] == s3[i+j] && dp[i+1][j] {
				dp[i][j] = true
			}
			if j < len(s2) && s2[j] == s3[i+j] && dp[i][j+1] {
				dp[i][j] = true
			}
		}
	}

	return dp[0][0]
}

// explanation: https://www.youtube.com/watch?v=3Rw3p9LrgvE
func isInterleaveDFS(s1 string, s2 string, s3 string) bool {
	if len(s3) != len(s1)+len(s2) {
		return false
	}

	memo := map[string]bool{}

	// k = i+j, k is current index at s3
	var dfs func(i, j int, memo map[string]bool) bool
	dfs = func(i, j int, memo map[string]bool) bool {
		key := fmt.Sprintf("%d,%d", i, j)

		if canInterleave, ok := memo[key]; ok {
			return canInterleave
		}

		if i == len(s1) && j == len(s2) {
			return true
		}

		if i < len(s1) && s1[i] == s3[i+j] {
			if dfs(i+1, j, memo) {
				return true
			}
		}

		if j < len(s2) && s2[j] == s3[i+j] {
			if dfs(i, j+1, memo) {
				return true
			}
		}

		memo[key] = false
		return false
	}

	return dfs(0, 0, memo)
}
