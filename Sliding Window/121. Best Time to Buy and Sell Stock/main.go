package main

func maxProfit(prices []int) int {
	max := 0
	i, j := 0, 1

	for j < len(prices) {
		if prices[i] > prices[j] {
			i = j
			j += 1
		} else {
			if v := prices[j] - prices[i]; v > max {
				max = v
			}

			j += 1
		}
	}

	return max
}

func maxProfitFast(prices []int) int {
	min := prices[0]
	profit := 0

	for i := range prices {
		if prices[i]-min > profit {
			profit = prices[i] - min
		}
		if prices[i] < min {
			min = prices[i]
		}
	}
	return profit
}
