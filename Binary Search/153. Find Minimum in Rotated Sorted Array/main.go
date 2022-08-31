// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
package main

import (
	"math"
)

// Example 1:
// Input: nums = [3,4,5,1,2]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times.

// Example 2:
// Input: nums = [4,5,6,7,0,1,2]
// Output: 0
// Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

// Example 3:
// Input: nums = [11,13,15,17]
// Output: 11
// Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

// You must write an algorithm that runs in O(log n) time.

func findMin(nums []int) int {
	min := math.MaxInt
	l, r := 0, len(nums)-1

	isRotated := nums[0] > nums[len(nums)-1]
	if !isRotated {
		return nums[0]
	}

	for l <= r {
		mid := (l + r) / 2
		if nums[mid] < min {
			min = nums[mid]
		}

		if nums[mid] >= nums[l] && nums[r] < nums[l] {
			l = mid + 1
		} else /* right portion part */ {
			r = mid - 1
		}
	}

	return min
}

// Explanation: https://www.youtube.com/watch?v=nIVW4P8b1VA
func findMinBetter(nums []int) int {
	min := nums[0]
	l, r := 0, len(nums)-1

	for l <= r {
		if nums[l] < nums[r] {
			if nums[l] < min {
				min = nums[l]
			}
			break
		}

		mid := (l + r) / 2
		if nums[mid] < min {
			min = nums[mid]
		}

		// left portion
		if nums[mid] >= nums[l] {
			l = mid + 1
		} else /* right portion part */ {
			r = mid - 1
		}
	}

	return min
}
