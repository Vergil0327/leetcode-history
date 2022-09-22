// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
package main

import "math"

// Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
// Finding the maximum subarray is standard and can be done greedily.
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/2136555/C%2B%2BPython-Simple-Solution-w-Explanation-or-Sliding-Window
func minOperations(nums []int, x int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	target := sum - x

	longest := 0
	found := false
	sum = 0
	l := 0
	for r := range nums {
		sum += nums[r]

		for l <= r && sum > target {
			sum -= nums[l]
			l += 1
		}

		if sum == target {
			found = true
			longest = max(longest, r-l+1)
		}
	}

	if found {
		return len(nums) - longest
	}
	return -1
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

// prefixSum[left] + suffixSum[right] == x
func minOperationsReverseHashmap(nums []int, x int) int {
	presumIdxMap := map[int]int{} // prefixSum: index
	presumIdxMap[0] = -1

	prefixSum := 0
	for i, num := range nums {
		prefixSum += num
		// 避免重複，而且僅需紀錄最靠左的index (求min operations)
		if _, ok := presumIdxMap[prefixSum]; !ok {
			presumIdxMap[prefixSum] = i
		}
	}

	ops := math.MaxInt

	// check prefix sum == x, suffixSum == 0
	if _, ok := presumIdxMap[x]; ok {
		ops = presumIdxMap[x] + 1
	}

	suffixSum := 0
	for j := len(nums) - 1; j >= 0; j-- {
		suffixSum += nums[j]
		preSum := x - suffixSum

		if i, ok := presumIdxMap[preSum]; ok && i < j /* can't overlap */ {
			ops = min(ops, i+1+len(nums)-j)
		}
	}

	if ops == math.MaxInt {
		return -1
	}

	return ops
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
