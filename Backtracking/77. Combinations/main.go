package main

func combine(n int, k int) [][]int {
	candidates := []int{}
	for i := 1; i <= n; i++ {
		candidates = append(candidates, i)
	}

	res := [][]int{}
	var dfs func(state []int, i, count int)
	dfs = func(state []int, i, count int) {
		if count == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)
			res = append(res, cpy)
			return
		}

		if i == len(candidates) || count < 0 {
			return
		}

		dfs(state, i+1, count)                          // skip i-th candidate
		dfs(append(state, candidates[i]), i+1, count-1) // take i-th candidate
	}
	dfs([]int{}, 0, k)

	return res
}

func combineAnother(n int, k int) [][]int {
	candidates := []int{}
	for i := 1; i <= n; i++ {
		candidates = append(candidates, i)
	}

	res := [][]int{}
	var dfs func(state []int, i, count int)
	dfs = func(state []int, i, count int) {
		if count == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)
			res = append(res, cpy)
			return
		}

		if i == len(candidates) || count < 0 {
			return
		}

		for j := i; j < len(candidates); j++ {
			dfs(append(state, candidates[j]), j+1, count-1) // try every combination. candidates[j] + [candidates[j+1] ... candidates[n-1]]
		}
	}
	dfs([]int{}, 0, k)

	return res
}
