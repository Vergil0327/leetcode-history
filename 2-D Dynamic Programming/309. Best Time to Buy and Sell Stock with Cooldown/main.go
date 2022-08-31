// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
package main

import (
	"fmt"
	"math"
)

/*
Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

					1, 2, 3, 0, 2
			buy
		 sell
 cooldown
	profit:0	-> B, -1 -> S:1  -> C:1	 -> B:1
										 -> C:-1 -> S:2	 -> C:2
										 				 -> C:-1 -> S:-2
						-> C, 0	 -> B:-2 -> C:-2
														 -> S:1
										 -> C:0	 -> B:-3
										 				 -> C:0
*/

// explanation: https://www.youtube.com/watch?v=I7j0F7AHpb8
// T:O(n)
func maxProfit(prices []int) int {
	// state: Buy or Sell?
	// if Buy: i+1
	// if Sell: i+2 (force to cooldown one day)

	memo := map[string]int{}

	var dfs func(i int, buying bool) int
	dfs = func(i int, buying bool) int {
		if i >= len(prices) {
			return 0
		}

		key := fmt.Sprintf("%d,%t", i, buying)
		if profit, ok := memo[key]; ok {
			return profit
		}

		if buying {
			buy := dfs(i+1, !buying) - prices[i]
			cooldown := dfs(i+1, buying)
			memo[key] = int(math.Max(float64(buy), float64(cooldown)))
		} else {
			sell := dfs(i+2, !buying) + prices[i]
			cooldown := dfs(i+1, buying)
			memo[key] = int(math.Max(float64(sell), float64(cooldown)))
		}

		return memo[key]
	}

	return dfs(0, true)
}

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
// T:O(n) M:O(n)
// other thinking: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/Share-my-thinking-process
func maxProfitDP(prices []int) int {
	if len(prices) <= 1 {
		return 0
	}

	//  state1 -> [buy] -> state2 -> [sell] -> state3 -> [cooldown] -> state1...
	//  |  ^						   |  ^
	//  |__|							 |__|
	// cooldown (we don't buy/sell)
	state1, state2, state3 := make([]int, len(prices)), make([]int, len(prices)), make([]int, len(prices))

	/* base case, value will be i-th profit */
	// can buy
	state1[0] = 0
	// can sell, after buy, you should have -prices[0] profit. Be positive!
	state2[0] = -prices[0]
	// cooldown
	state3[0] = math.MinInt // lower base case

	for i := 1; i < len(prices); i++ {
		state1[i] = int(math.Max(float64(state1[i-1]), float64(state3[i-1])))
		state2[i] = int(math.Max(float64(state2[i-1]), float64(state1[i-1]-prices[i]))) // don't sell or buy from state1
		state3[i] = state2[i-1] + prices[i]
	}

	return int(math.Max(float64(state1[len(prices)-1]), float64(state3[len(prices)-1])))
}

/*
As the state transitions only involve limited states and steps,
we should be able to improve the space complexity to O(1):

int maxProfit(vector<int>& prices) {
    int sold = 0, hold = INT_MIN, rest = 0;
    for (int i=0; i<prices.size(); ++i)
    {
        int prvSold = sold;
        sold = hold + prices[i];
        hold = max(hold, rest-prices[i]);
        rest = max(rest, prvSold);
    }
    return max(sold, rest);
}
M:O(1)
*/
func maxProfitDP_Optimized(prices []int) int {
	sold, hold, reset := 0, math.MinInt, 0
	for i := 0; i < len(prices); i++ {
		prevSold := sold
		sold = hold + prices[i]
		hold = int(math.Max(float64(hold), float64(reset-prices[i]))) // don't buy just cooldown, buy prices[i](max profit state transited from reset to hold)
		reset = int(math.Max(float64(reset), float64(prevSold)))
	}

	return int(math.Max(float64(sold), float64(reset)))
}
