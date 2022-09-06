// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

package main

import (
	"fmt"
	"math"
)

// intuition of state transfer function
// 可參考: https://www.youtube.com/watch?v=gsL3T9bI1RQ
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
func maxProfit(prices []int) int {
	hold1, sold1, hold2, sold2 := math.MinInt, 0, math.MinInt, 0

	// our 4 hold position state transfer functions, we want our profit to be maximum,
	// so we use max() in each state
	// because we can just hold at each operation, we can stay at previous state at any operation (i.e. max(prevState, newState))
	for i := 0; i < len(prices); i++ {
		hold1Prev, sold1Prev, hold2Prev, sold2Prev := hold1, sold1, hold2, sold2

		hold1 = max(hold1Prev, -prices[i])
		sold1 = max(sold1Prev, hold1Prev+prices[i])
		hold2 = max(hold2Prev, sold1Prev-prices[i])
		sold2 = max(sold2Prev, hold2+prices[i])
	}

	return max(sold1, sold2) // we can choose not to buy/sell second time
}

func maxProfitOther(prices []int) int {
	buy1, buy2 := math.MaxInt, math.MaxInt
	sell1, sell2 := 0, 0

	for i := 0; i < len(prices); i++ {
		buy1 = min(buy1, prices[i])
		sell1 = max(sell1, prices[i]-buy1) // gains when selling first time
		buy2 = min(buy2, prices[i]-sell1)  // find something in behind that is smaller, to get a negative value here
		sell2 = max(sell2, prices[i]-buy2) // get biggest value + second gain
	}
	return sell2
}

/*
First Try
Runtime: 4253 ms, faster than 5.39% of Go online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 92.4 MB, less than 5.39% of Go online submissions for Best Time to Buy and Sell Stock III.
*/
// T:O(n^2) maybe?, reduce 2^n to n^2 because each subproblem we only calculate once and we only buy/sell two choices
// therefore, total # of subproblem is n and each with 2 choices
func maxProfitSlow(prices []int) int {
	memo := map[string]int{}

	var dfs func(i, txTimes int, isBuying bool) int
	dfs = func(i, txTimes int, isBuying bool) int {
		if i == len(prices) || txTimes == 0 {
			return 0
		}

		key := fmt.Sprintf("%d,%d,%t", i, txTimes, isBuying)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		if !isBuying {
			memo[key] = max(dfs(i+1, txTimes, !isBuying)-prices[i], dfs(i+1, txTimes, isBuying))
			return memo[key]
		} else {
			memo[key] = max(dfs(i+1, txTimes-1, !isBuying)+prices[i], dfs(i+1, txTimes, isBuying))
			return memo[key]
		}
	}
	return dfs(0, 2, false)
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a >= b {
		return b
	}
	return a
}
