// https://leetcode.com/problems/jump-game/
package main

/*
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
*/

// [3,2,1,0,4]
// [1]
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
