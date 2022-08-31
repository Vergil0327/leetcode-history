// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
package main

// https://www.youtube.com/watch?v=3SJ3pUkPQMc&t=15s
func maxProfit(prices []int) int {
	profit := 0
	for i := 1; i < len(prices); i++ {
		if p := prices[i] - prices[i-1]; p > 0 {
			profit += p
		}
	}

	return profit
}
