// https://leetcode.com/problems/longest-increasing-subsequence/
package main

import "math"

/*
def lengthOfLIS(self, nums):

	tails = [0] * len(nums)
	size = 0
	for x in nums:
	    i, j = 0, size
	    while i != j:
	        m = (i + j) / 2
	        if tails[m] < x:
	            i = m + 1
	        else:
	            j = m
	    tails[i] = x
	    size = max(i + 1, size)
	return size
*/
func lengthOfLIS_Optimized(nums []int) int {
	tails := make([]int, len(nums))
	size := 0

	for _, num := range nums {
		i, j := 0, size
		for i < j {
			mid := i + (j-i)/2
			if tails[mid] < num {
				i = mid + 1
			} else {
				j = mid
			}
		}

		tails[i] = num
		size = int(math.Max(float64(i+1), float64(size))) // or if i == size {size+=1}
	}

	return size
}

// explanation: https://leetcode.com/problems/longest-increasing-subsequence/
// T:O(n*n)
// there is also an nLog(n) solution: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
func lengthOfLIS_DP(nums []int) int {
	LIS := make([]int, len(nums))
	for i := 0; i < len(LIS); i++ {
		LIS[i] = 1
	}

	for i := len(nums) - 1; i >= 0; i-- {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] < nums[j] {
				LIS[i] = int(math.Max(float64(LIS[i]), float64(1+LIS[j])))
			}
		}
	}

	max := 1
	for _, length := range LIS {
		if length > max {
			max = length
		}
	}
	return max
}

// brute force T:O(2^n)
func lengthOfLIS(nums []int) int {
	max := 0
	var dfs func(i, count int)
	dfs = func(i, count int) {
		if i == len(nums)-1 {
			if count > max {
				max = count
			}
		}

		for j := i + 1; j < len(nums); j++ {
			if nums[j] > nums[i] {
				dfs(j, count+1)
			}
		}

		// !!! check current count after iteration finished
		if count > max {
			max = count
		}
	}

	for i := 0; i < len(nums); i++ {
		dfs(i, 1)
	}

	return max
}
