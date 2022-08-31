// https://leetcode.com/problems/find-the-duplicate-number/
package main

/*
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

nums[0] -> nums[1] -> nums[3] -> nums[2]-> nums[4]
																		^					|
																		|_ _ _ _ _|

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
*/

// Explanation: https://www.youtube.com/watch?v=wjYnzkAhcNk
// Linked List Cycle Problem
// Floyd's Algorithm (slow fast pointer)
func findDuplicate(nums []int) int {
	slow, fast := 0, 0
	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast {
			break
		}
	}

	slow2 := 0
	for {
		slow = nums[slow]
		slow2 = nums[slow2]
		if slow == slow2 {
			break
		}
	}
	return slow
}
