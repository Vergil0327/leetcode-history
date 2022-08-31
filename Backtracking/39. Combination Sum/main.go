// https://leetcode.com/problems/combination-sum/
package main

import (
	"fmt"
	"sort"
)

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
		dfs(state, i, total+candidates[i])
		state = state[:len(state)-1]
		dfs(state, i+1, total)
	}

	dfs([]int{}, 0, 0)

	return solutions
}

// ---------------------

func combinationSum2(candidates []int, target int) [][]int {
	solutions := [][]int{}
	sort.Slice(candidates, func(i, j int) bool {
		return candidates[i] < candidates[j]
	})

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

		for i := i; i < len(candidates); i++ {
			state = append(state, candidates[i])
			dfs(state, i, total-candidates[i])
			state = state[:len(state)-1]
		}
	}

	dfs([]int{}, 0, target)

	return solutions
}

// we need to remove duplicate
// Input: [2,3,6,7], 7
// Output: [[2,2,3],[2,3,2],[3,2,2],[7]]
// Expected: [[2,2,3],[7]]
// T:O(2^target)
// explanation: https://www.youtube.com/watch?v=GBKI9VSKdGg
func combinationSumSlowAndWrong(candidates []int, target int) [][]int {
	solutions := [][]int{}
	existed := []map[int]int{}

	var dfs func(state []int)
	dfs = func(state []int) {
		if sum(state) > target {
			return
		}
		if checkIfStateValid(state, target) {
			cpy := make([]int, len(state))
			copy(cpy, state)

			m := map[int]int{}
			for _, v := range cpy {
				m[v] += 1
			}

			for _, checkMap := range existed {
				if fmt.Sprint(checkMap) == fmt.Sprint(m) {
					return
				}
			}

			solutions = append(solutions, cpy)
			existed = append(existed, m)
			return
		}

		for _, candidate := range candidates {
			state = append(state, candidate)
			dfs(state)
			state = state[:len(state)-1]
		}
	}

	dfs([]int{})
	return solutions
}

func checkIfStateValid(state []int, target int) bool {
	return sum(state) == target
}

func sum(state []int) int {
	sum := 0
	for _, v := range state {
		sum += v
	}
	return sum
}
