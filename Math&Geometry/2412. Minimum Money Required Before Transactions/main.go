// https://leetcode.com/problems/minimum-money-required-before-transactions/
package main

import (
	"sort"
)

// https://leetcode.com/problems/minimum-money-required-before-transactions/discuss/2588034/JavaC%2B%2BPython-Easy-and-Coincise
// T:O(n)
func minimumMoneyOptimized(transactions [][]int) int64 {
	// sum of all money we can lose
	totalCost := 0

	// The worst case is losing all money first, then we earn money later.
	minMoneyToEarn := 0
	minMoneyToLose := 0
	for _, tx := range transactions {
		cost, cashback := tx[0], tx[1]
		totalCost += max(0, cost-cashback)

		// see above, total += cost-cashback
		// 	worst case for losing money transaction is:
		// 			we spend all of money before last tx, before getting cashback, so we need to add cashback to cost and the cashback should be largest
		//	worst case for earning money transaction is:
		// 			the first tx is largest cost
		//
		// code below can combine to one line one variable: minMoney = max(minMoney, min(cost, cashback)) // we always find the maximum lower value between cost & cashback
		if cashback >= cost {
			minMoneyToEarn = max(minMoneyToEarn, cost)
		} else {
			minMoneyToLose = max(minMoneyToLose, cashback)
		}
	}

	return int64(totalCost + max(minMoneyToEarn, minMoneyToLose))
}

// https://leetcode.com/problems/minimum-money-required-before-transactions/discuss/2587905/Python-Explanation-with-pictures-Greedy
// nlogn
func minimumMoney(transactions [][]int) int64 {
	makeMoney := [][]int{}
	loseMoney := [][]int{}
	for _, tx := range transactions {
		cost, cashback := tx[0], tx[1]
		if cost > cashback {
			loseMoney = append(loseMoney, tx)
		} else {
			makeMoney = append(makeMoney, tx)
		}
	}

	sort.Slice(makeMoney, func(i, j int) bool {
		return makeMoney[i][0] > makeMoney[j][0]
	})
	sort.Slice(loseMoney, func(i, j int) bool {
		return loseMoney[i][1] < loseMoney[j][1]
	})

	// if we want all of the transactions can be completed regardless of the order of the transactions,
	// think of worst case: lose money first and earning larger cashback last
	peakCost := 0
	costChange := 0
	for _, tx := range loseMoney {
		costChange += tx[0]
		peakCost = max(peakCost, costChange)
		costChange -= tx[1]
	}

	// minimum money situation: money we left after losing money is equal to max cost of makeMoney
	if len(makeMoney) > 0 {
		costChange += makeMoney[0][0]
	}

	// 1st situation: we have higher cost peak than final cost. i.e. we've already had enough money for max cost of makeMoney transaction.
	// 2nd situation: our max cost of makeMoney transactions is greater than losingMoney cost
	// we need to choose max cost to meet the minimum money requirement
	return int64(max(costChange, peakCost))
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
