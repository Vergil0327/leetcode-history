package main

import (
	"sort"
)

/*
	Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
	You must implement a solution with a linear runtime complexity and use only constant extra space.
*/

// T(n)=O(NlogN)+O(n), M(1)
func singleNumber(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	sort.Ints(nums) // O(NlogN)

	// O(n)
	for len(nums) > 1 {
		if nums[0] == nums[1] {
			nums = nums[2:]
		} else {
			return nums[0]
		}
	}

	return nums[0]
}

// using XOR operator
// see: https://youtu.be/qMPX1AOa83k
func singleNumberBetter(nums []int) int {
	bit := nums[0]
	for i := 1; i < len(nums); i++ {
		bit ^= nums[i]
	}

	return bit
}
