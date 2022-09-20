// https://leetcode.com/problems/move-zeroes/

package main

func moveZeroes(nums []int) {
	l, r := 0, 0
	for r < len(nums) {
		for l < r && nums[l] != 0 {
			l += 1
		}

		if nums[r] != 0 {
			nums[r], nums[l] = nums[l], nums[r]
		}
		r += 1
	}
}
