// https://leetcode.com/problems/search-in-rotated-sorted-array
package main

// Example 1:
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

// Example 2:
// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

// Example 3:
// Input: nums = [1], target = 0
// Output: -1
// ! You must write an algorithm with O(log n) runtime complexity.

// [4,5,6,7,0,1,2]
// if mid == 6 and target > mid, search RIGHT portion
// if mid == 6 and target < mid, two conditions:
// 		if target < left-most, search RIGHT portion
// 		if target >= left-most, search LEFT portion
// if mid == 1 and target < mid, search LEFT portion
// if mid == 1 and target > mid, two conditions
// 		if target <= right-most, search RIGHT portion
// 		if target > right-most, search LEFT portion
// https://www.youtube.com/watch?v=U8XENwh8Oy8
// T:O(logN)
func search(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l <= r /* using `<=` can check [1] */ {
		mid := l + (r-l)/2

		if nums[mid] == target {
			return mid
		}

		// left sorted portion
		if nums[mid] >= nums[l] {
			if target > nums[mid] {
				l = mid + 1
			} else if /* target < nums[mid] && */ target < nums[l] {
				l = mid + 1
			} else /* target > nums[l] */ {
				r = mid - 1
			}
		} else /* right sorted array */ {
			if target < nums[mid] {
				r = mid - 1
			} else if target > nums[r] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
	}

	return -1
}

func searchBetter(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l <= r /* using `<=` can check [1] */ {
		mid := l + (r-l)/2

		if nums[mid] == target {
			return mid
		}

		// left sorted portion
		if nums[mid] >= nums[l] {
			if target > nums[mid] || target < nums[l] {
				l = mid + 1
			} else /* target > nums[l] */ {
				r = mid - 1
			}
		} else {
			if target < nums[mid] || target > nums[r] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
	}

	return -1
}

// T:O(n + log(n-m) + log(m))
func searchWrong(nums []int, target int) int {
	if len(nums) < 1 {
		return -1
	}

	pivot := 0
	for i, v := range nums {
		if i > 0 && v < nums[i-1] {
			pivot = i
		}
	}

	bot, top := 0, pivot-1
	for bot <= top {
		mid := top - (top-bot)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			top = mid - 1
		} else {
			bot = mid + 1
		}
	}

	bot, top = pivot, len(nums)-1
	for bot <= top {
		mid := top - (top-bot)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			top = mid - 1
		} else {
			bot = mid + 1
		}
	}

	return -1
}
