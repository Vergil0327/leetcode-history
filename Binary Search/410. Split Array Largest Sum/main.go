// https://leetcode.com/problems/split-array-largest-sum/
package main

import "math"

// https://www.youtube.com/watch?v=YUF3_eBdzsk
// T:O(nlog(S)), S is sum of nums
func splitArray(nums []int, m int) int {
	l, r := 0, 0 // max(nums), sum(nums) => our search space
	for _, num := range nums {
		l = max(l, num)
		r += num
	}

	for l < r {
		mid := l + (r-l)/2
		if canSplit(nums, mid, m) {
			r = mid
		} else {
			l = mid + 1
		}
	}

	return l
}

// return true if we can split into m group and each group's sum is less than sum
func canSplit(nums []int, largestSum, m int) bool {
	subarray := 0
	currSum := 0

	for _, num := range nums {
		currSum += num
		if currSum > largestSum {
			subarray += 1
			currSum = num
		}
	}

	// totoal subarray is subarray + 1, don't forget last iteration
	subarray += 1

	return subarray <= m
}

// DP T:O(n^2*m)
func splitArrayBacktracking(nums []int, m int) int {
	memo := map[[2]int]int{}

	var dfs func(i, m int) int
	dfs = func(i, m int) int {
		if m == 1 {
			return sum(nums[i:])
		}

		if cacheSum, ok := memo[[2]int{i, m}]; ok {
			return cacheSum
		}

		res, currSum := math.MaxInt, 0
		for j := i; j < len(nums)-m+1; j++ {
			currSum += nums[j]
			maxSum := max(currSum, dfs(j+1, m-1))
			res = min(res, maxSum)
			if currSum > res {
				break
			}
		}
		memo[[2]int{i, m}] = res
		return res
	}

	return dfs(0, m)
}

func sum(nums []int) (total int) {
	for _, num := range nums {
		total += num
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
