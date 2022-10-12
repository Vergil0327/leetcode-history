// https://leetcode.com/problems/coin-change/
package main

import "math"

/*
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
*/

// T:O(n) M:O(n)
// idea: https://youtu.be/oBt53YbR9Kk
func coinChange(coins []int, amount int) int {
	// ! edge case
	if amount == 0 {
		return 0
	}

	dp := make([][]int, amount+1)
	dp[0] = []int{}

	for i := 0; i <= amount; i++ {
		if dp[i] != nil {
			for _, coin := range coins {
				newCoins := append(dp[i], coin)
				if i+coin <= amount && (dp[i+coin] == nil || len(newCoins) < len(dp[i+coin])) {
					dp[i+coin] = newCoins
				}
			}
		}
	}

	if len(dp[amount]) > 0 {
		return len(dp[amount])
	} else {
		return -1
	}
}

// https://leetcode.com/problems/coin-change/discuss/1475250/Python-4-solutions%3A-Top-down-DP-Bottom-up-DP-Space-O(amount)-Clean-and-Concise
func coinChangeTopDown(coins []int, amount int) int {
	memo := map[[2]int]int{}
	var dfs func(i, amount int) int
	dfs = func(i, amount int) int {
		if amount == 0 {
			memo[[2]int{i, amount}] = 0
			return 0
		}

		if i >= len(coins) {
			memo[[2]int{i, amount}] = math.MaxInt
			return math.MaxInt
		}

		if _, ok := memo[[2]int{i, amount}]; ok {
			return memo[[2]int{i, amount}]
		}

		ans := dfs(i+1, amount) // skip

		if amount >= coins[i] { // used
			v := dfs(i, amount-coins[i])
			if v != math.MaxInt {
				// if v == math.MaxInt, v+1 will overflow
				ans = min(ans, v+1)
			}
		}

		memo[[2]int{i, amount}] = ans
		return ans
	}

	if count := dfs(0, amount); count == math.MaxInt {
		return -1
	} else {
		return count
	}
}

// we don't really cache index of coin we used
func coinChangeTopDownOptimized(coins []int, amount int) int {
	memo := map[int]int{}

	var dfs func(amount int) int
	dfs = func(amount int) int {
		if amount == 0 {
			return 0
		}

		if _, ok := memo[amount]; ok {
			return memo[amount]
		}

		used := math.MaxInt
		for _, coin := range coins {
			// prune the invalid choices
			if amount >= coin {
				if count := dfs(amount - coin); count != math.MaxInt {
					used = min(used, 1+count)
				}
			}
		}

		memo[amount] = used
		return used
	}

	if used := dfs(amount); used == math.MaxInt {
		return -1
	} else {
		return used
	}
}

func min(nums ...int) int {
	min := math.MaxInt
	for _, v := range nums {
		if v < min {
			min = v
		}
	}

	return min
}

// explanation: https://www.youtube.com/watch?v=H9bfqozjoqs
func coinChangeOtherDP(coins []int, amount int) int {
	dp := make([]int, amount+1)
	dp[0] = 0
	for i := 1; i < amount+1; i++ {
		dp[i] = amount + 1 // default value
	}

	for amt := 1; amt < amount+1; amt++ {
		for _, coin := range coins {
			if amt-coin >= 0 {
				dp[amt] = int(math.Min(float64(dp[amt]), float64(1+dp[amt-coin])))
			}
		}
	}

	if val := dp[amount]; val != amount+1 /* not equal to default value */ {
		return val
	} else {
		return -1
	}
}
