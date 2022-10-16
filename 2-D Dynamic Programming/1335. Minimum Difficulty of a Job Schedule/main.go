package main

import "math"

// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution
// T: O(n*n*d), d is tree height and loop n with findMax
func minDifficulty(jobDifficulty []int, d int) int {
	N := len(jobDifficulty)
	if N < d {
		return -1
	}

	memo := map[[2]int]int{}

	// i is split index, this is prefix DP
	// [..., i, ...], find max within A[:i]
	var dfs func(i, d int) int
	dfs = func(i, d int) int {
		if d == 1 {
			return max(jobDifficulty[i:]...)
		}

		if _, ok := memo[[2]int{i, d}]; ok {
			return memo[[2]int{i, d}]
		}

		res := math.MaxInt
		maxDif := 0

		// try every subarray
		// O(n*n)
		for j := i; j < N-d+1; j++ {
			maxDif = max(maxDif, jobDifficulty[j]) // O(n)
			res = min(res, maxDif+dfs(j+1, d-1))
		}

		memo[[2]int{i, d}] = res
		return res
	}

	return dfs(0, d)
}

// O(n)
func max(arr ...int) int {
	v := math.MinInt
	for _, num := range arr {
		if num > v {
			v = num
		}
	}

	return v
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
