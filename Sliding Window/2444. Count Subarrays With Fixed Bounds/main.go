package main

import "math"

// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/discuss/2708099/JavaC%2B%2BPython-Sliding-Window-with-Explanation
// T:O(n)
func countSubarrays(nums []int, minK int, maxK int) int64 {
	res := 0
	iMin, iMax := -1, -1
	l := 0
	for r := 0; r < len(nums); r++ {
		// subarray is invalid, reset min & max position
		// also move j ponter at new start position
		if nums[r] < minK || nums[r] > maxK {
			iMin, iMax = -1, -1
			l = r + 1
		}
		if nums[r] == minK {
			iMin = r
		}
		if nums[r] == maxK {
			iMax = r
		}

		// valid subarray would be [l, min(iMin, iMax)]
		res += max(0, min(iMin, iMax)-l+1)
	}

	return int64(res)
}

// n * n!
// I don't know how to solve it, so I try them all. (Brute Force)
// since I got TLE by bracktrcking, I try DP technique to cache result
// it works !
func countSubarraysDP(nums []int, minK int, maxK int) int64 {
	set := map[int][]int{} // val: [index]
	for i, num := range nums {
		if set[num] == nil {
			set[num] = make([]int, 0)
		}
		set[num] = append(set[num], i)
	}

	// if minK or maxK didn't exist in nums
	if _, ok := set[minK]; !ok {
		return 0
	}
	if _, ok := set[maxK]; !ok {
		return 0
	}

	memo := map[[3]int]int{}

	var dfs func(minState, maxState int, i int) int
	dfs = func(minState, maxState, i int) int {
		if i == len(nums) {
			if minState == minK && maxState == maxK {
				return 1
			}
			return 0
		}

		if _, ok := memo[[3]int{minState, maxState, i}]; ok {
			return memo[[3]int{minState, maxState, i}]
		}

		if minState == minK && maxState == maxK {

			// return 1+dfs( min(minState, nums[i]), max(maxState, nums[i]), i+1)
			memo[[3]int{minState, maxState, i}] = 1 + dfs(min(minState, nums[i]), max(maxState, nums[i]), i+1)
			return memo[[3]int{minState, maxState, i}]
		} else if minState >= minK && maxState <= maxK { // if not valid, keep exploring subarray
			memo[[3]int{minState, maxState, i}] = dfs(min(minState, nums[i]), max(maxState, nums[i]), i+1)
			return memo[[3]int{minState, maxState, i}]
		}

		memo[[3]int{minState, maxState, i}] = 0
		return memo[[3]int{minState, maxState, i}]
		// dfs(min(minState, nums[i]), max(maxState, nums[i]), i+1)
	}

	// [1,2,3]
	// we'll try
	// [1] -> dfs -> [1,2] -> dfs -> [1,2,3]
	// [2], [2,3]
	// [3]
	var res int64
	for i := 0; i < len(nums); i++ {
		res += int64(dfs(math.MaxInt, math.MinInt, i))
	}

	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
