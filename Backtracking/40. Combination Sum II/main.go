// https://leetcode.com/problems/combination-sum-ii/
package main

import "sort"

// explanation: https://www.youtube.com/watch?v=rSA3t6BDDwg
// all the combination sum include current pick
// & all the combination sum NOT include current pick
func combinationSum2(candidates []int, target int) [][]int {
	solutions := [][]int{}

	// sorting for duplicate check afterwards
	sort.Ints(candidates)

	var dfs func(state []int, target int, start int)
	dfs = func(state []int, target int, start int) {
		if target == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		if target < 0 {
			return
		}

		prevCandidate := -1
		for i := start; i < len(candidates); i++ {
			if prevCandidate == candidates[i] /* which means duplicate */ {
				continue
			}
			state = append(state, candidates[i])
			dfs(state, target-candidates[i], i+1)
			state = state[:len(state)-1]

			prevCandidate = candidates[i]
		}
	}

	dfs([]int{}, target, 0)
	return solutions
}

// all the combination sum include current pick
// & all the combination sum NOT include current pick
func combinationSum2Another(candidates []int, target int) [][]int {
	sort.Ints(candidates) // O(nlogn)
	solutions := [][]int{}

	var dfs func(state []int, target int, i int)
	dfs = func(state []int, target int, i int) {
		if target == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		if i >= len(candidates) || target < 0 {
			return
		}

		if candidates[i] > target {
			return
		}

		next := i + 1
		for next < len(candidates) && candidates[next] == candidates[i] {
			next += 1
		}
		dfs(state, target, next)                                     // skip current one and its duplicate
		dfs(append(state, candidates[i]), target-candidates[i], i+1) // use current one only once
	}

	dfs([]int{}, target, 0)
	return solutions
}

func combinationSum2Counter(candidates []int, target int) [][]int {
	solutions := [][]int{}

	var dfs func(state []int, target int, start int, counter [][]int)
	dfs = func(state []int, target int, start int, counter [][]int) {
		if target == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		if target < 0 {
			return
		}

		for i := start; i < len(counter); i++ {
			entry := counter[i]
			if entry[1] <= 0 {
				continue
			}

			state = append(state, entry[0])
			counter[i][1] -= 1
			dfs(state, target-counter[i][0], i, counter)
			state = state[:len(state)-1]
			counter[i][1] += 1
		}
	}

	countMap := map[int]int{}
	for _, candidate := range candidates {
		countMap[candidate] += 1
	}

	counter := make([][]int, len(countMap)) // [[candidate1, count], ...]
	i := 0
	for candidate, count := range countMap {
		counter[i] = []int{candidate, count}
		i += 1
	}

	dfs([]int{}, target, 0, counter)
	return solutions
}
