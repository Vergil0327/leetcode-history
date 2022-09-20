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

/*
A simple realization is if the current element is non-0, its' correct position can at best be it's current position or a position earlier. If it's the latter one, the current position will be eventually occupied by a non-0 ,or a 0, which lies at a index greater than 'cur' index. We fill the current position by 0 right away,so that unlike the previous solution, we don't need to come back here in next iteration.

In other words, the code will maintain the following invariant:
 1. All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
 2. All elements between the current and slow pointer are zeroes.

Therefore, when we encounter a non-zero element, we need to swap elements pointed by current and slow pointer, then advance both pointers. If it's zero element, we just advance current pointer.
With this invariant in-place, it's easy to see that the algorithm will work.
*/
func moveZeroesConcise(nums []int) {
	lastNonZeroAt := 0
	for curr := 0; curr < len(nums); curr++ {
		if nums[curr] != 0 {
			nums[curr], nums[lastNonZeroAt] = nums[lastNonZeroAt], nums[curr]
			lastNonZeroAt += 1
		}
	}
}
