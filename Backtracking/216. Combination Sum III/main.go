package main

func combinationSum3(k int, n int) [][]int {
	candidates := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	res := [][]int{}

	var dfs func(state []int, i, count, target int)
	dfs = func(state []int, i, count, target int) {
		if count == 0 && target == 0 {
			cpy := make([]int, len(state))
			copy(cpy, state)
			res = append(res, cpy)
			return
		}
		if i >= len(candidates) || count < 0 || target < 0 {
			return
		}

		dfs(state, i+1, count, target)                                        // skip i-th candidate
		dfs(append(state, candidates[i]), i+1, count-1, target-candidates[i]) // take i-th candidate
	}
	dfs([]int{}, 0, k, n)

	return res
}
