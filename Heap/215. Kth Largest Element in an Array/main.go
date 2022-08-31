// https://leetcode.com/problems/kth-largest-element-in-an-array/
package main

// Quick Select Algorithm
// average: T:O(n) worst: T:O(n^2)
// explanation: https://www.youtube.com/watch?v=s8p8ukTyA2I
func findKthLargest(nums []int, k int) int {
	targetIdx := len(nums) - k

	var quickSelect func(l, r int) int
	quickSelect = func(l, r int) int {
		pivot, p := nums[r], l
		for i := l; i < r; i++ {
			if nums[i] <= pivot {
				nums[i], nums[p] = nums[p], nums[i]
				p++
			}
		}
		nums[p], nums[r] = pivot, nums[p]

		if targetIdx > p {
			return quickSelect(p+1, r)
		} else if targetIdx < p {
			return quickSelect(l, p-1)
		} else {
			return nums[p]
		}
	}

	return quickSelect(0, len(nums)-1)
}
