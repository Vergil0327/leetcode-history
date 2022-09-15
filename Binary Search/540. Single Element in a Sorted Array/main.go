// https://leetcode.com/problems/single-element-in-a-sorted-array/
package main

// huahua: https://www.youtube.com/watch?v=uJa9Q-05JxY
// pair value will follow the rule that
// another pair's index = index + 1 if index is even else index -1
// even position's index is odd, vice versa
// if single element is on the right side of middle, it won't break the rule in left portion,
// we can use this to do binary search
func singleNonDuplicate(nums []int) int {
	l, r := 0, len(nums)-1

	for l < r {
		mid := l + (r-l)/2
		var pair int
		if mid&1 == 0 /* is even */ {
			pair = mid + 1
		} else {
			pair = mid - 1
		}

		if nums[mid] == nums[pair] {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return nums[l]
}
