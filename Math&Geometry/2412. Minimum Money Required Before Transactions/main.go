// https://leetcode.com/problems/minimum-money-required-before-transactions/
package main

import "sort"

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
