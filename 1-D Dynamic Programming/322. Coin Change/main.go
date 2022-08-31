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
