// https://leetcode.com/problems/burst-balloons/

package main

import (
	"fmt"
	"math"
)

// https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
// The iterative approach is very tricky to do correctly, though.. but easy if we think from the base case:
//
//   - Bottom-up approaches always starts from the base cases and builds upward
//   - Base-case is: when left+1 == right, then return 0. A.k.a. there are no balloons in the middle to pop. So these base case values are already stored in our DP array!
//   - The next case is when we have only 1 balloon between left and right. k represents the distance between left and right, and k = 2 means that there is one balloon between left and right
//   - So first we iterate through the entire array and find every result when there is just 1 ballon between left and right, and when that's finished, increase the distance k between left and right
//   - Notice that dp line assigns dp[left][right] to nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
//   - dp[left][i] and dp[i][right]) when k=2 are equal to the base cases! Equals 0! We are always referencing values from the previous iterations.
//   - Keep increasing the number of balloons in between left and right, until we reach the final case left = 0 and right=n-1
func maxCoins(nums []int) int {
	nums = append([]int{1}, append(nums, 1)...)

	dp := make([][]int, len(nums))
	for i := range dp {
		dp[i] = make([]int, len(nums))
	}

	// compute all possible sizes as subarray of size len needs to know results for len-1, len-2 and etc.
	for k := 2; k < len(nums); k++ {
		for l := 0; l < len(nums)-k; l++ {
			r := l + k
			for i := l + 1; i < r; i++ {
				coins := nums[l]*nums[i]*nums[r] + dp[l][i] + dp[i][r]
				dp[l][r] = int(math.Max(float64(dp[l][r]), float64(coins)))
			}
		}
	}

	return dp[0][len(nums)-1]
}

// comes from Top-Down solution
// T:O(N^3) M:O(N^2)
func maxCoinsBottomUp(nums []int) int {
	nums = append([]int{1}, append(nums, 1)...)

	dp := make([][]int, len(nums))
	for i := range dp {
		dp[i] = make([]int, len(nums))
	}

	// compute all possible sizes as subarray of size len needs to know results for len-1, len-2 and etc.
	// iterate through 1 to len(nums)-2
	originalN := len(nums) - 2
	for l := originalN; l >= 1; l-- {
		for r := l; r <= originalN; r++ {
			for i := l; i <= r; i++ {
				coins := nums[l-1]*nums[i]*nums[r+1] + dp[l][i-1] + dp[i+1][r]
				dp[l][r] = int(math.Max(float64(dp[l][r]), float64(coins)))
			}
		}
	}

	return dp[1][len(nums)-2]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// https://www.youtube.com/watch?v=VFskby7lUbw
// T:O(N^3) M:O(N^2)
// will timeout in 2022
func maxCoinsTopDown(nums []int) int {
	nums = append([]int{1}, append(nums, 1)...)
	dp := map[string]int{}

	var dfs func(l, r int) int
	dfs = func(l, r int) int {
		if l > r {
			return 0
		}

		key := fmt.Sprintf("%d,%d", l, r)
		if _, ok := dp[key]; ok {
			return dp[key]
		}

		// iterate through all possibilities within boundary
		// 1, [nums[l], ..., i, ..., nums[r]], 1
		// i-th num is the last number we pop from array
		for i := l; i < r+1; i++ {
			coins := nums[l-1] * nums[i] * nums[r+1]
			coins += dfs(l, i-1) + dfs(i+1, r) // left/right portion of subarray(sub-problems)
			dp[key] = int(math.Max(float64(dp[key]), float64(coins)))
		}

		return dp[key]
	}

	return dfs(1, len(nums)-2) // actual left/right boundary (not includes 1)
}
