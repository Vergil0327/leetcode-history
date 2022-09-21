// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
package main

import "math"

// we don't care about value after k, so we can just replace it
func removeDuplicatesOtherSolution(nums []int) int {
	var (
		count = 1
		j     = 0
	)

	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[j] {
			count += 1
			j += 1
			nums[j] = nums[i]
		}
	}
	return count
}

func removeDuplicates(nums []int) int {
	k := 0
	currMax := math.MinInt
	l, r := 0, 0
	for r < len(nums) {
		if nums[r] > currMax {
			currMax = nums[r]
			nums[l], nums[r] = nums[r], nums[l]
			l += 1
			k += 1
		}
		r += 1
	}

	return k
}
