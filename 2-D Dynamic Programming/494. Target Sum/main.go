// https://leetcode.com/problems/target-sum/
package main

import (
	"fmt"
	"math"
)

func findTargetSumWaysDP(nums []int, target int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}

	// sum < target: 永遠不可能達成
	// ! sum should be greater than |target| (math.Abs)
	// consider this case: nums:[100], target:-200
	if sum < int(math.Abs(float64(target))) {
		return 0
	}

	dp := make([][]int, len(nums)+1)
	OFFSET := sum
	for i := 0; i < len(nums)+1; i++ {
		// 取值範圍: 2*sum+1, 因為最大全正數，最小全負數，所以值的範圍是: -sum ~ +sum
		dp[i] = make([]int, sum+OFFSET+1)
	}
	dp[0][OFFSET] = 1

	for i := 1; i < len(nums)+1; i++ {
		for j := nums[i-1]; j < 2*sum+1-nums[i-1]; j++ {
			dp[i][j-nums[i-1]] += dp[i-1][j] // positive sign
			dp[i][j+nums[i-1]] += dp[i-1][j] // negative sign
		}
	}

	return dp[len(nums)][OFFSET+target] // ! remember offset
}

// https://leetcode.com/problems/target-sum/solution/
// https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C%2B%2B-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation
// recommend: https://www.youtube.com/watch?v=zks6mN06xdQ
func findTargetSumWaysDP_Optimized(nums []int, target int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}

	if sum < target || (target+sum)%2 > 0 {
		return 0
	} else {
		return subsetSum(nums, (target+sum)/2)
	}
}

func subsetSum(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1
	for _, num := range nums {
		for i := target; i >= num; i-- {
			dp[i] += dp[i-num]
		}
	}
	return dp[target]
}

// tracking total sum
// explanation: https://www.youtube.com/watch?v=g0npyaQtAQM
// Time complexity: O(t⋅n). t refers to the sum of the nums array and n refers to the length of the nums array.
// Space complexity: O(t⋅n).
func findTargetSumWaysBetter(nums []int, target int) int {
	memo := map[string]int{}

	var dfs func(i, sum int) int
	dfs = func(i, sum int) int {
		if i == len(nums) && sum == target {
			return 1
		}

		if i >= len(nums) {
			return 0
		}

		key := fmt.Sprintf("%d,%d", i, sum)

		if count, ok := memo[key]; ok {
			return count
		}

		nums[i] = -nums[i]
		rslt1 := dfs(i+1, sum+nums[i])

		nums[i] = -nums[i]
		rslt2 := dfs(i+1, sum+nums[i])

		memo[key] = rslt1 + rslt2
		return memo[key]
	}

	return dfs(0, 0)
}

/* first try */

func findTargetSumWays(nums []int, target int) int {
	memo := map[string]int{}

	var dfs func(i int) int
	dfs = func(i int) int {
		sum := Sum(nums)
		if i == len(nums) && sum == target {
			return 1
		}

		if i >= len(nums) {
			return 0
		}

		key := fmt.Sprintf("%d,%d", i, sum)

		if count, ok := memo[key]; ok {
			return count
		}

		nums[i] = -nums[i]
		rslt1 := dfs(i + 1)

		nums[i] = -nums[i]
		rslt2 := dfs(i + 1)

		memo[key] = rslt1 + rslt2
		return memo[key]
	}

	return dfs(0)
}

func Sum(nums []int) int {
	var sum int
	for _, num := range nums {
		sum += num
	}

	return sum
}
