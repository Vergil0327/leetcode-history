// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
package main

// leetcode: https://www.youtube.com/watch?v=4sQL7R5ySUU
func searchRangeLeetcode(nums []int, target int) []int {
	left := binSearch(nums, target, true)
	right := binSearch(nums, target, false)
	return []int{left, right}
}

func binSearch(nums []int, target int, leftBias bool) int {
	i := -1
	l, r := 0, len(nums)-1
	for l <= r {
		mid := l + (r-l)/2
		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			i = mid
			if leftBias {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
	}

	return i
}

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
