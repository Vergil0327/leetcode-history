// https://leetcode.com/problems/coin-change-2/
package main

import "fmt"

/*
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

explanation: https://www.youtube.com/watch?v=Mjy4hd2xgrs
*/

// we can further reduce our code since `nextDP[a] = dp[a]` looks redundant
// it's totally fine for us to replace nextDP with dp
func changeDP_Optimized_Compact(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1 // base case: always one way to acheive zero amount

	for i := 1; i < len(coins)+1; i++ {
		// nextDP := make([]int, amount+1) // ! redundant
		// nextDP[0] = 1 // ! redundant
		for a := 1; a < amount+1; a++ {
			// nextDP[a] = dp[a] // ! redundant
			if a-coins[i-1] >= 0 {
				// nextDP[a] += nextDP[a-coins[i-1]] // ! replace nextDP with dp
				dp[a] += dp[a-coins[i-1]]
			}
		}
		// dp = nextDP // ! redundant
	}

	return dp[amount]
}

// since our dp results only rely on i & i-1 row from coins,
// we can optimize space complexity to O(n)
func changeDP_Optimized(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1 // base case: always one way to acheive zero amount

	for i := 1; i < len(coins)+1; i++ {
		nextDP := make([]int, amount+1)
		nextDP[0] = 1
		for a := 1; a < amount+1; a++ {
			nextDP[a] = dp[a]
			if a-coins[i-1] >= 0 {
				nextDP[a] += nextDP[a-coins[i-1]]
			}
		}
		dp = nextDP
	}

	return dp[amount]
}

// T:O(m*n) M:O(m*n)
func changeDP(amount int, coins []int) int {
	dp := make([][]int, len(coins)+1)
	for i := 0; i < len(coins)+1; i++ {
		dp[i] = make([]int, amount+1)
	}

	/* base case: always one way to acheive zero amount */
	for i := 0; i < len(coins)+1; i++ {
		dp[i][0] = 1
	}

	for i := 1; i < len(coins)+1; i++ {
		for a := 1; a < amount+1; a++ {
			dp[i][a] = dp[i-1][a] // skip i-th coin
			if a-coins[i-1] >= 0 {
				dp[i][a] += dp[i][a-coins[i-1]] // take coin at i index (which means plus 0...i-1 coin's results)
			}
		}
	}

	return dp[len(coins)][amount]
}

// T:O(m*n) M:O(m*n)
func changeDFS_MEMO(amount int, coins []int) int {
	memo := map[string]int{}

	var dfs func(i, target int) int
	dfs = func(i, target int) int {
		if target == 0 {
			return 1
		}

		if target < 0 || i >= len(coins) {
			return 0
		}

		key := fmt.Sprintf("%d,%d", i, target)
		if combination, ok := memo[key]; ok {
			return combination
		}

		var sum int
		sum += dfs(i, target-coins[i]) + dfs(i+1, target)

		memo[key] = sum
		return sum
	}

	return dfs(0, amount)
}
