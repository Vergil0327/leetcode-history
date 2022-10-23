package main

import "sort"

func minMoves2(nums []int) int {
	sort.Ints(nums)

	median := nums[len(nums)/2]
	moves := 0
	for _, num := range nums {
		moves += abs(median - num)
	}

	return moves
}

func abs(num int) int {
	if num < 0 {
		return -num
	}

	return num
}
