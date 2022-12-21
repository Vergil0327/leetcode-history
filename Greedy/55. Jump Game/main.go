// https://leetcode.com/problems/jump-game/
package main

func canJump(nums []int) bool {
	pos := 0
	jump := nums[0]
	for jump > 0 {
		if pos == len(nums)-1 {
			return true
		}

		jump -= 1
		pos += 1

		if jump < nums[pos] {
			jump = nums[pos]
		}
	}

	return pos >= len(nums)-1
}

func canJumpReverseThinking(nums []int) bool {
	goal := len(nums) - 1
	for i := len(nums) - 1; i >= 0; i-- {
		if i+nums[i] >= goal {
			goal = i
		}
	}

	return goal == 0
}
