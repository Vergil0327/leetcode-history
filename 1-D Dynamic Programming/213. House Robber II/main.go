// https://leetcode.com/problems/house-robber-ii/
package main

import (
	"math"
)

// T:O(n) M:O(1)
// solution: https://www.youtube.com/watch?v=rWAJCfYYOvM
func robBetter(nums []int) int {
	var robI = func(nums []int) int {
		rob1, rob2 := 0, 0
		for _, num := range nums {
			newRob := int(math.Max(float64(rob1+num), float64(rob2)))
			rob1 = rob2
			rob2 = newRob
		}

		return rob2
	}

	return int(math.Max(
		float64(nums[0]), math.Max(float64(robI(nums[1:])), float64(robI(nums[:len(nums)-1])))),
	)
}

// robII(i) = max(rob(0:n-1), rob(1:n))
// rob(i) = max(rob(i-1), rob(i-2)+nums[i])
//
// rob(0:n-1):max(rob(n-2), rob(n-3)+ nums[n-1])
// rob(1:n):max(rob(n-1), rob(n-2)+nums[n])
//
// Input: [2,3,2]
// Expected: 3
// Input: [1,2,3]
// Expected: 3
// Input: [1,2,3,1]
// Expected: 4
// Input: [0]
// Expected: 0
// Input: [1]
// Expected: 1
// T:O(n) M:O(n)
func rob(nums []int) int {
	// !fucking edge case
	if len(nums) == 1 {
		return nums[0]
	}

	return int(math.Max(float64(robI(nums[:len(nums)-1])), float64(robI(nums[1:]))))
}

func robI(nums []int) int {
	dp := make([]int, len(nums)+1)
	dp[0] = 0
	dp[1] = nums[0]
	for i := 1; i < len(nums); i++ {
		dp[i+1] = int(math.Max(float64(dp[i-1]+nums[i]), float64(dp[i])))
	}

	return dp[len(nums)]
}
