// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
package main

// T:O(n^2) M:O(1), only M,P,G as key in hash map
func garbageCollection(garbage []string, travel []int) int {
	time := 0

	travelMostFar := map[rune]int{}
	for i, g := range garbage {
		for _, c := range g {
			travelMostFar[c] = i
			time += 1
		}
	}

	for _, v := range travelMostFar {
		for i := 0; i <= v-1; i++ {
			time += travel[i]
		}
	}

	return time
}

func garbageCollectionOther(garbage []string, travel []int) int {
	time := 0

	aggregateTravel := make([]int, len(travel)+1)
	for i := 1; i < len(travel)+1; i++ {
		aggregateTravel[i] = travel[i-1] + aggregateTravel[i-1]
	}

	travelMostFar := map[rune]int{}
	for i, g := range garbage {
		for _, c := range g {
			travelMostFar[c] = aggregateTravel[i]
			time += 1
		}
	}

	for _, v := range travelMostFar {
		time += v
	}

	return time
}
