// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
package main

// T:O(logn)
func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}

	// find upper bound: nums[mid] <= target
	// find lower bound: nums[mid] >= target
	l, r := 0, len(nums)-1
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	lowerBound := l

	if nums[l] != target {
		return []int{-1, -1}
	}

	l, r = 0, len(nums)-1
	for l < r {
		mid := r - (r-l)/2
		if nums[mid] > target {
			r = mid - 1
		} else {
			l = mid
		}
	}
	upperBound := r

	return []int{lowerBound, upperBound}
}
