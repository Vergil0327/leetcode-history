// https://leetcode.com/problems/find-peak-element/
package main

func findPeakElementBetter(nums []int) int {
	l, r := 0, len(nums)-1
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] < nums[mid+1] {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return l
}

func findPeakElement(nums []int) int {
	l, r := 0, len(nums)-1

	peak := -1
	for l <= r {
		mid := l + (r-l)/2
		midR := mid + 1
		if mid+1 >= len(nums) {
			midR = mid
		}

		if nums[mid] < nums[midR] {
			l = mid + 1
			peak = mid + 1
		} else {
			r = mid - 1
			peak = mid
		}
	}

	return peak
}
