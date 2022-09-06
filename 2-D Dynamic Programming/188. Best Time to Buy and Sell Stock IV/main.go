// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

package main

import "math"

// Idea From Best Time To Buy And Sell Stock III:
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54125/Very-understandable-solution-by-reusing-Problem-III-idea

// other reference: https://www.youtube.com/watch?v=lXRe__YD8JY

// T:O(n*k) T:O(k)
func maxProfit(k int, prices []int) int {
	buy := make([]int, k+1)
	sell := make([]int, k+1)
	for i := range buy {
		buy[i] = math.MinInt // make first buy reasonable according to recurrence
	}

	/*
		transaction: 1, 2, ..., tx-1, tx
						buy: state of buy[tx] can come from buy[tx] and sell[tx-1] - price. (not buy & buy from previous sell)
					 sell: state of sell[tx] can come from not sell (sell[tx]) and sell from previous buy (buy[tx] + price)
	*/
	for _, p := range prices {
		for tx := 1; tx <= k; tx++ {
			buy[tx] = max(buy[tx], sell[tx-1]-p)
			sell[tx] = max(sell[tx], buy[tx]+p)
		}
	}

	return sell[k]
}

// T:O(n*k) T:O(k)
func maxProfitOptimized(k int, prices []int) int {
	buy := make([]int, k+1)
	sell := make([]int, k+1)
	for i := range buy {
		buy[i] = math.MinInt // make first buy reasonable according to recurrence
	}

	// if k >= n/2, then you can make maximum number of transactions
	// we can arbitrarily buy and sell
	if k >= len(prices)/2 {
		profit := 0
		for i := 0; i < len(prices)-1; i++ {
			if p := prices[i+1] - prices[i]; p > 0 {
				profit += p
			}
		}

		return profit
	}

	/*
		transaction: 1, 2, ..., tx-1, tx
						buy: state of buy[tx] can come from buy[tx] and sell[tx-1] - price. (not buy & buy from previous sell)
					 sell: state of sell[tx] can come from not sell (sell[tx]) and sell from previous buy (buy[tx] + price)
	*/
	for _, p := range prices {
		for tx := 1; tx <= k; tx++ {
			buy[tx] = max(buy[tx], sell[tx-1]-p)
			sell[tx] = max(sell[tx], buy[tx]+p)
		}
	}

	return sell[k]
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
