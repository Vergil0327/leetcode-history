// https://leetcode.com/problems/house-robber/
package main

import (
	"math"
)

/*
Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Disscusion: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems./209401
*/

// Input: [1,2,3,1]
// Expected: 4
// Input: [2,7,9,3,1]
// Expected: 12
// Input: [0]
// Expected: 0
// Input: [1,1]
// Expected: 1
// Input: [1,3,1]
// Expected: 3
// Input: [2,1,1,2]
// Expected: 4
// rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
// T:O(n) M: O(n)
func rob(nums []int) int {
	dp := make([]int, len(nums)+1)
	dp[0] = 0
	dp[1] = nums[0]

	for i := 1; i < len(nums); i++ {
		dp[i+1] = int(math.Max(float64(nums[i]+dp[i-1]), float64(dp[i])))
	}

	return dp[len(nums)]
}

// T:O(n) M: O(1)
// according to upper solution, we only need three variables: prev, curr, num
// dp[i-1](prev), dp[i](curr) and nums[i](num) to derived dp[i+1]
// prev, curr, num
// Input: [2,1,1,2]
// Expected: 4
// round 1: curr = Max(0+2, 0), prev = 0
// round 2: curr = Max(0+1, 2), prev = 2
// round 3: curr = Max(2+1, 1), prev = 2
// round 4: curr = Max(2+2, 3), prev = 3
func robOpitimize(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	curr, prev := 0, 0
	for _, num := range nums {
		tmp := curr
		curr = int(math.Max(float64(prev+num), float64(curr)))
		prev = tmp
	}

	return curr
}
