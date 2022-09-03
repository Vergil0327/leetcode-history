// https://leetcode.com/problems/edit-distance/
package main

import (
	"fmt"
	"math"
)

/*
MIT Course Explanation: https://www.youtube.com/watch?v=ocZMDMZwhCY
- subproblem: suffix, x[i:] & y[j:]
- # of subproblems: |x|*|y|
- guess:
 1. replace x[i] -> y[j]
 2. insert y[j]
 3. delete x[i]

- recurrence: DP(i, j) = min(
 1. cost of replace x[i]->y[j] + DP[i+1,j+1]
 2. cost of insert y[j] + DP[i, j+1]
 3. cost of delete x[i] + DP[i+1,j])
*/
// neetcode: https://www.youtube.com/watch?v=XYi2-LPrwm4
func minDistanceBottomUp(word1 string, word2 string) int {
	dp := make([][]int, len(word1)+1)
	for i := range dp {
		dp[i] = make([]int, len(word2)+1)
	}

	// base case: word1[i:] <-> word2[j:]
	// "" <-> ""
	dp[len(word1)][len(word2)] = 0

	// base case: "abc" or "bc" or "c" <-> ""
	for i := len(word1) - 1; i >= 0; i-- {
		dp[i][len(word2)] = len(word1) - i
	}

	// base case: "" <-> "abc" or "bc" or "c"
	for j := len(word2) - 1; j >= 0; j-- {
		dp[len(word1)][j] = len(word2) - j
	}

	// bottom-up
	for i := len(word1) - 1; i >= 0; i-- {
		for j := len(word2) - 1; j >= 0; j-- {
			if word1[i] == word2[j] {
				dp[i][j] = dp[i+1][j+1]
			} else {
				replace := 1 + dp[i+1][j+1] // replace x[i] -> y[j]
				insert := 1 + dp[i][j+1]    // insert y[j]
				del := 1 + dp[i+1][j]       // delete x[i]
				dp[i][j] = int(math.Min(math.Min(float64(replace), float64(insert)), float64(del)))
			}
		}
	}
	return dp[0][0]
}

// [[3 3 4 5]
//
//	[3 2 3 4]
//	[2 2 2 3]
//	[3 2 1 2]
//	[3 2 1 1]
//	[3 2 1 0]]
//
// space-optimized: https://leetcode.com/problems/edit-distance/discuss/25846/C%2B%2B-O(n)-space-DP
func minDistance(word1 string, word2 string) int {
	dp := make([]int, len(word2)+1)
	dpPrev := make([]int, len(word2)+1)

	// base case for dpPrev
	for i := len(word2) - 1; i >= 0; i-- {
		dpPrev[i] = len(word2) - i
	}

	// ? how to setup base case for dp?
	// for i := len(word1) - 1; i >= 0; i-- {
	// 	dp[i][len(word2)] = len(word1) - i
	// }

	for i := len(word1) - 1; i >= 0; i-- {
		dp[len(word2)] = len(word1) - i // ! base case for dp!!!
		for j := len(word2) - 1; j >= 0; j-- {
			// !!! still compare word1[i] == word[j] rather than word1[j]==word2[j]
			if word1[i] == word2[j] {
				// dp[i][j] = dp[i+1][j+1]
				dp[j] = dpPrev[j+1]
			} else {
				// replace := 1 + dp[i+1][j+1] // replace x[i] -> y[j]
				// insert := 1 + dp[i][j+1]    // insert y[j]
				// del := 1 + dp[i+1][j]       // delete x[i]
				// dp[i][j] = int(math.Min(math.Min(float64(replace), float64(insert)), float64(del)))
				replace := 1 + dpPrev[j+1]
				insert := 1 + dp[j+1]
				del := 1 + dpPrev[j]
				dp[j] = int(math.Min(math.Min(float64(replace), float64(insert)), float64(del)))
			}
		}

		dp, dpPrev = dpPrev, dp
	}
	return dpPrev[0]
}

// https://leetcode.com/problems/edit-distance/discuss/1475220/Python-3-solutions-Top-down-DP-Bottom-up-DP-O(N)-in-Space-Clean-and-Concise
// T:O(m*n) M:O(m*n)
func minDistanceTopDown(word1 string, word2 string) int {
	memo := map[string]int{}

	var dfs func(i, j int, memo map[string]int) int
	dfs = func(i, j int, memo map[string]int) int {
		// "" <-> "", "abc" <-> "abc"
		if (i == len(word1) && j == len(word2)) || word1 == word2 {
			return 0
		}

		// "" <-> "abc"
		if i == len(word1) /* word1[i:] == "" */ {
			return len(word2) - j // insert ops
		}

		// "abc" <-> ""
		if j == len(word2) /* word2[j:] == "" */ {
			return len(word1) - i // delete ops
		}

		key := fmt.Sprintf("%d,%d", i, j)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		if word1[i] == word2[j] {
			memo[key] = dfs(i+1, j+1, memo)
			return memo[key]
		} else {
			// replace x[i] with y[j]
			replace := 1 + dfs(i+1, j+1, memo)

			// insert y[j]
			insert := 1 + dfs(i, j+1, memo)

			// delete x[i]
			del := 1 + dfs(i+1, j, memo)

			memo[key] = int(math.Min(math.Min(float64(replace), float64(insert)), float64(del)))
			return memo[key]
		}
	}

	return dfs(0, 0, memo)
}

func minDistanceTopDownTimeout(word1 string, word2 string) int {
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		// "" <-> "", "abc" <-> "abc"
		if (i == len(word1) && j == len(word2)) || word1 == word2 {
			return 0
		}

		// "" <-> "abc"
		if i == len(word1) /* word1[i:] == "" */ {
			return len(word2) - j // insert ops
		}

		// "abc" <-> ""
		if j == len(word2) /* word2[j:] == "" */ {
			return len(word1) - i // delete ops
		}

		if word1[i] == word2[j] {
			return dfs(i+1, j+1)
		} else {
			// replace x[i] with y[j]
			replace := 1 + dfs(i+1, j+1)

			// insert y[j]
			insert := 1 + dfs(i, j+1)

			// delete x[i]
			del := 1 + dfs(i+1, j)

			return int(math.Min(math.Min(float64(replace), float64(insert)), float64(del)))
		}
	}

	return dfs(0, 0)
}
