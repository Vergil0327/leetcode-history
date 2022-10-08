// https://leetcode.com/problems/combination-sum/
package main

// Input: candidates = [2,3,6,7], target = 7
// Output: [[2,2,3],[7]]
// Explanation:
// 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
// 7 is a candidate, and 7 = 7.
// These are the only two combinations.

func combinationSum(candidates []int, target int) [][]int {
	solutions := [][]int{}

	var dfs func(state []int, i int, total int)
	dfs = func(state []int, i int, total int) {
		if total > target || i >= len(candidates) {
			return
		}

		if total == target {
			cpy := make([]int, len(state))
			copy(cpy, state)

			solutions = append(solutions, cpy)
			return
		}

		state = append(state, candidates[i])
		dfs(state, i, total+candidates[i]) // take i-th candidate and we can take again
		state = state[:len(state)-1]
		dfs(state, i+1, total) // skip current
	}

	dfs([]int{}, 0, 0)

	return solutions
}

// ---------------------

func combinationSum2(candidates []int, target int) [][]int {
	solutions := [][]int{}
	// sort.Slice(candidates, func(i, j int) bool {
	// 	return candidates[i] < candidates[j]
	// })

	var dfs func(state []int, i int, total int)
	dfs = func(state []int, i int, total int) {
		if total < 0 {
			return
		}

		if total == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)

			solutions = append(solutions, cpy)
			return
		}

		// combination: use i = 0, ..., n to form combination
		// use i = 1, ..., n
		// ...
		// use i = n-1, n
		// use i = n
		for i := i; i < len(candidates); i++ {
			state = append(state, candidates[i])
			dfs(state, i, total-candidates[i])
			state = state[:len(state)-1]
		}
	}

	dfs([]int{}, 0, target)

	return solutions
}
