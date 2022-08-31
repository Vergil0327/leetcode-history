package main

import "math"

// explanation: https://www.youtube.com/watch?v=ktmzAZWkEZ0

// Input: cost = [10,15,20]
// Output: 15
// Explanation: You will start at index 1.
// - Pay 15 and climb two steps to reach the top.
// The total cost is 15.

// Constraints:
// 2 <= cost.length <= 1000
// 0 <= cost[i] <= 999
func minCostClimbingStairs(cost []int) int {
	cost = append(cost, 0) // for math works

	for i := len(cost) - 3; i >= 0; i-- {
		cost[i] = int(math.Min(float64(cost[i]+cost[i+1]), float64(cost[i]+cost[i+2])))
		// or cost[i] += int(math.Min(float64(cost[i+1]), float64(cost[i+2])))
	}

	return int(math.Min(float64(cost[0]), float64(cost[1])))
}
