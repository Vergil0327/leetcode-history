package main

import "fmt"

// once we jump to the last stone, stop exploring and return True
func canCross(stones []int) bool {
	if stones[1] != 1 {
		return false
	}

	memo := map[string]bool{}

	var dfs func(i, unit int) bool
	dfs = func(i, unit int) bool {
		if i == len(stones)-1 {
			return true
		}

		key := fmt.Sprintf("%d,%d", i, unit)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		// explore all the possible stone that we can jump onto
		for j := i + 1; j < len(stones); j++ {
			if stones[j] == stones[i]+unit-1 {
				if dfs(j, unit-1) {
					return true
				}
			}

			if stones[j] == stones[i]+unit {
				if dfs(j, unit) {
					return true
				}
			}

			if stones[j] == stones[i]+unit+1 {
				if dfs(j, unit+1) {
					return true
				}
			}
		}

		memo[key] = false
		return false
	}
	return dfs(1, 1)
}

// https://leetcode.com/problems/frog-jump/discuss/193816/Concise-and-fast-DP-solution-using-2D-array-instead-of-HashMap-with-text-and-video-explanation.
func canCrossBottomUp(stones []int) bool {
	N := len(stones)

	dp := make([][]bool, N) // dp[position][jump unit]
	for i := range dp {
		dp[i] = make([]bool, N+1)
	}
	dp[0][1] = true

	for i := 1; i < N; i++ {
		for j := 0; j < i; j++ {
			diff := stones[i] - stones[j]
			if diff < 0 || diff > N {
				continue // out of bounds
			}

			if dp[j][diff] {
				if diff-1 >= 0 {
					dp[i][diff-1] = true
				}
				dp[i][diff] = true
				if diff+1 <= N {
					dp[i][diff+1] = true
				}

				// reach last stone
				if i == N-1 {
					return true
				}
			}
		}
	}

	return false
}
