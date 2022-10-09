package main

func combinationSum4(nums []int, target int) int {
	memo := map[int]int{}
	var dfs func(state int) int
	dfs = func(state int) int {
		if state == target {
			memo[state] = 1
			return memo[state]
		}
		if state > target {
			memo[state] = 0
			return memo[state]
		}

		if _, ok := memo[state]; ok {
			return memo[state]
		}

		// since we can reuse every num in nums
		// for-loop always starts from 0 to the end
		total := 0
		for i := 0; i < len(nums); i++ {
			total += dfs(state + nums[i])
		}

		memo[state] = total
		return memo[state]
	}

	return dfs(0)
}
