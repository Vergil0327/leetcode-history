// https://leetcode.com/problems/maximum-number-of-robots-within-budget/
package main

import "math"

// Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
// Output: 3
// Explanation:
// It is possible to run all individual and consecutive pairs of robots within budget.
// To obtain answer 3, consider the first 3 robots. The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
// It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.
// max(chargeTimes) + k * sum(runningCosts)

// sliding window + 239. Sliding Window Maximum
// T:O(n) M:O(n)
func maximumRobots(chargeTimes []int, runningCosts []int, budget int64) int {
	N := len(chargeTimes)
	robot := 0

	// monotonically decreasing
	dequeue := []int{}

	sum := 0
	l, r := 0, 0
	for r < N {
		sum += runningCosts[r]

		for len(dequeue) > 0 && chargeTimes[dequeue[len(dequeue)-1]] <= chargeTimes[r] {
			dequeue = dequeue[:len(dequeue)-1]
		}
		dequeue = append(dequeue, r)

		if (r-l+1)*sum+chargeTimes[dequeue[0]] > int(budget) {
			if l == dequeue[0] {
				dequeue = dequeue[1:]
			}
			sum -= runningCosts[l]
			l += 1
		} else {
			robot = int(math.Max(float64(robot), float64(r-l+1)))
		}

		r += 1
	}

	return robot
}

// we don't need robot variable because window size always keeps possible maximum
func maximumRobotsOptimized(chargeTimes []int, runningCosts []int, budget int64) int {
	N := len(chargeTimes)

	// monotonically increasing
	dequeue := []int{}

	sum := 0
	l, r := 0, 0
	for r < N {
		sum += runningCosts[r]

		for len(dequeue) > 0 && chargeTimes[dequeue[len(dequeue)-1]] <= chargeTimes[r] {
			dequeue = dequeue[:len(dequeue)-1]
		}
		dequeue = append(dequeue, r)

		if (r-l+1)*sum+chargeTimes[dequeue[0]] > int(budget) {
			if l == dequeue[0] {
				dequeue = dequeue[1:]
			}
			sum -= runningCosts[l]
			l += 1
		}

		r += 1
	}

	return N - l
}
