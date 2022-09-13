// https://leetcode.com/problems/ugly-number-ii/
package main

// explanation: https://www.youtube.com/watch?v=ZG86C_U-vRg
// ugly number is a set from {1...i2 * 2, 1...i3 * 3, 1...i5 * 5}
func nthUglyNumber(n int) int {
	nums := []int{1}
	i2, i3, i5 := 0, 0, 0
	for len(nums) < n {
		next2 := nums[i2] * 2
		next3 := nums[i3] * 3
		next5 := nums[i5] * 5
		nextMin := min(min(next2, next3), next5)
		if nextMin == next2 {
			i2 += 1
		}
		if nextMin == next3 {
			i3 += 1
		}
		if nextMin == next5 {
			i5 += 1
		}
		nums = append(nums, nextMin)
	}

	return nums[len(nums)-1]
}

func min(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
