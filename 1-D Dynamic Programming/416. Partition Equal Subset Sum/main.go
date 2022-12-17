// https://leetcode.com/problems/partition-equal-subset-sum/
package main

// explanation: https://www.youtube.com/watch?v=IsvocB5BJhw
func canPartitionOptimized(nums []int) bool {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%2 != 0 {
		return false
	}

	target := float64(sum) / 2
	dp := map[int]bool{0: true}

	for _, num := range nums {
		nextDP := map[int]bool{}
		for val := range dp {
			// early return at the moment we find target
			if num+val == int(target) {
				return true
			}

			// can't update dp while iteration
			nextDP[num+val] = true
			nextDP[val] = true
		}
		dp = nextDP
	}

	return dp[int(target)]
}
func canPartition(nums []int) bool {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum%2 != 0 {
		return false
	}

	target := float64(sum) / 2
	dp := map[int]bool{0: true}

	for _, num := range nums {
		nextDP := map[int]bool{}
		for val := range dp {
			// can't update dp while iteration
			nextDP[num+val] = true
			nextDP[val] = true
		}
		dp = nextDP
	}

	return dp[int(target)]
}

// DFS+Memo: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
func canPartitionDFS(nums []int) bool {
	sum := 0
	for _, num := range nums {
		sum += num
	}

	if sum%2 != 0 {
		return false
	}

	target := sum / 2
	memo := make(map[int]map[int]bool, len(nums))
	for i := 0; i < len(nums); i++ {
		memo[i] = make(map[int]bool, target+1)
	}

	var dfs func(i int, target int, memo map[int]map[int]bool) bool
	dfs = func(i, target int, memo map[int]map[int]bool) bool {
		if hasTarget, ok := memo[i][target]; ok {
			return hasTarget
		}

		if target == 0 {
			return true
		}

		if i == len(nums) || target < 0 {
			// ! OUT OF BOUND ERROR
			// we don't need this: memo[i][target] = false
			return false
		}

		// pick nums[i]
		if dfs(i+1, target-nums[i], memo) {
			return true
		}

		// don't pick nums[i]
		if dfs(i+1, target, memo) {
			return true
		}

		memo[i][target] = false
		return false
	}

	return dfs(0, target, memo)
}
