// https://leetcode.com/problems/maximum-product-subarray/
package main

import (
	"math"
)

/*
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Input: nums = [2,3,-2,4,-5]
Output: 240

Input: nums = [2,3,-2,4,5]
Output: 20
*/

// explanation: https://www.youtube.com/watch?v=lXVy6YWFcRM
// T:O(n) M:O(1)
func maxProductDPOptimize(nums []int) int {
	result := math.MinInt
	for _, num := range nums {
		if num > result {
			result = num
		}
	}

	currMax, currMin := 1, 1

	for i := 0; i < len(nums); i++ {
		tmpMax := nums[i] * currMax
		currMax = int(math.Max(float64(nums[i]), math.Max(float64(nums[i]*currMin), float64(tmpMax))))
		currMin = int(math.Min(float64(nums[i]), math.Min(float64(nums[i]*currMin), float64(tmpMax))))
		result = int(math.Max(float64(result), float64(currMax)))
	}

	return result
}

// T:O(n) M:O(3n)
func maxProductDP(nums []int) int {
	dp := make([]int, len(nums)+1)
	dpMax := make([]int, len(nums)+1)
	dpMin := make([]int, len(nums)+1)
	dp[0] = nums[0] // default value: max(num in nums)
	for _, num := range nums {
		if num > dp[0] {
			dp[0] = num
		}
	}
	dpMax[0] = 1
	dpMin[0] = 1

	for i := 0; i < len(nums); i++ {
		dpMax[i+1] = int(math.Max(float64(nums[i]), math.Max(float64(nums[i]*dpMin[i]), float64(nums[i]*dpMax[i]))))
		dpMin[i+1] = int(math.Min(float64(nums[i]), math.Min(float64(nums[i]*dpMin[i]), float64(nums[i]*dpMax[i]))))
		dp[i+1] = int(math.Max(float64(dp[i]), math.Max(float64(nums[i]*dpMax[i]), float64(nums[i]*dpMin[i]))))
	}

	return dp[len(nums)]
}

// brute force
// T:O(n^2)
func maxProduct(nums []int) int {
	max := nums[0]
	for i := 0; i < len(nums); i++ {
		product := nums[i]
		if product > max {
			max = product
		}
		for j := i + 1; j < len(nums); j++ {
			if product *= nums[j]; product > max {
				max = product
			}
		}
	}

	return max
}
