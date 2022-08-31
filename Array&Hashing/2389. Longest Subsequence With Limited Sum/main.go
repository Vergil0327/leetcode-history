// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

package main

import (
	"sort"
)

// T:O(nLog(n) + m*n), n for size of nums and m for size of queries
func answerQueries(nums []int, queries []int) []int {
	ans := []int{}
	sort.Ints(nums)

	for _, q := range queries {
		size := 0
		for i := 0; i < len(nums); i++ {
			q -= nums[i]
			if q < 0 {
				break
			}
			size += 1
		}
		ans = append(ans, size)
	}
	return ans
}

// explanation: https://leetcode.com/problems/longest-subsequence-with-limited-sum/discuss/2492737/Prefix-Sum
// T:O(mLog(n))
func answerQueriesBetter(nums []int, queries []int) []int {
	ans := []int{}
	sort.Ints(nums)

	// n
	aggregate := make([]int, len(nums)+1)
	for i := 1; i < len(nums)+1; i++ {
		aggregate[i] = aggregate[i-1] + nums[i-1]
	}

	// mLog(n)
	for _, q := range queries {
		// log(n)
		l, r := 0, len(aggregate)-1
		for l < r {
			mid := r - (r-l)/2
			if aggregate[mid] > q {
				r = mid - 1
			} else {
				l = mid
			}
		}
		ans = append(ans, l)
	}
	return ans
}
