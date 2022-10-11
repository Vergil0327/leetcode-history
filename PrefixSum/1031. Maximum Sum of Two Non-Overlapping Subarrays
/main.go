package main

import "math"

/*
firstLen sum -> L, secondLen sum -> M
overeall max = max(L max + M, M max + L)

explanation: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/279221/JavaPython-3-two-easy-DP-codes-w-comment-time-O(n)-NO-change-of-input
*/
func maxSumTwoNoOverlapOptimized(nums []int, firstLen int, secondLen int) int {
	prefixSum := make([]int, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		prefixSum[i+1] = prefixSum[i] + nums[i]
	}

	L, M := firstLen, secondLen

	// we need to swap L and M to scan twice, since either subarray can occur before the other
	return max(maxSum(prefixSum, L, M), maxSum(prefixSum, M, L))
}

func maxSum(p []int, L, M int) (ans int) {
	// ans only comes from maxL + sum of M subarray
	for i, maxL := L+M, 0; i < len(p); i++ {
		maxL = max(maxL, p[i-M]-p[i-M-L]) // update max of L-length subarray
		ans = max(ans, maxL+p[i]-p[i-M])  // update max of the sum of L-length & M-length subarrays
	}

	return
}

func max(arr ...int) int {
	var max = math.MinInt
	for _, v := range arr {
		if v > max {
			max = v
		}
	}
	return max
}

// Brute Force: O(n^2)
func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) int {
	prefixSum := make([]int, len(nums)+1)
	for i, num := range nums {
		prefixSum[i+1] = prefixSum[i] + num
	}

	maxSum := math.MinInt
	for i := firstLen - 1; i < len(nums); i++ {
		sum := (prefixSum[i+1] - prefixSum[i+1-firstLen])

		for j := secondLen - 1; j < len(nums); j++ {
			// first subarray range: [i-firstLen+1, i]
			// second subarray range: [j-secondLen+1, j]
			if j < i-firstLen+1 || j-secondLen+1 > i {
				totalSum := sum + (prefixSum[j+1] - prefixSum[j+1-secondLen])
				if totalSum > maxSum {
					maxSum = totalSum
				}
			}
		}
	}

	return maxSum
}
