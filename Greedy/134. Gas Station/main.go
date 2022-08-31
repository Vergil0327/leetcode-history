// https://leetcode.com/problems/gas-station/
package main

/*
Example 1:
Input:
 gas = [1,2,3,4,5],
cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
*/

// gas =  [1,2,3,4,5]
// cost = [3,4,5,1,2]
// 				-2,-2,-2,3,3
// Output: 3

// greedy assumption:
// important: there is only one uniq solution if sum(gas) >= sum(cost)
// the farthest station where all the stations after A-station can arrived is A station if we can start from A-station
// thus, if there is a B-station comes after A, it CAN'T be solution
// http://bookshadow.com/weblog/2015/08/06/leetcode-gas-station/
// 如果是個數值變化是個週期, 那累積最小值的下一個位置必為最大值的開始
func canCompleteCircuit(gas []int, cost []int) int {
	totalGas, totalCost := 0, 0
	for i := 0; i < len(gas); i++ {
		totalGas += gas[i]
		totalCost += cost[i]
	}

	if totalGas < totalCost {
		return -1
	}

	total := 0
	start := 0
	for i := 0; i < len(gas); i++ {
		total += gas[i] - cost[i]
		if total < 0 {
			total = 0
			start = (i + 1) % len(gas)
		}
	}

	return start
}

// brute force ----> TIMEOUT
func canCompleteCircuitBruteForce(gas []int, cost []int) int {
	// append for circular
	STATION_COUNT := len(gas)

	gas = append(gas, gas...)
	cost = append(cost, cost...)

	var tank int
	for i := 0; i < STATION_COUNT; i++ {
		for j := i; j < len(gas); j++ {
			tank += gas[j]
			tank -= cost[j]
			if tank < 0 {
				tank = 0
				break
			}
			if j == i+STATION_COUNT {
				return i
			}
		}
	}

	return -1
}
