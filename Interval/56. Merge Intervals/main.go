// https://leetcode.com/problems/merge-intervals/
package main

import (
	"math"
	"sort"
)

/*
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

explanation: https://www.youtube.com/watch?v=44H3cEC2fFM
*/

// T:O(nlog(n)+n)
func mergeBetter(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	res := [][]int{}

	for _, interval := range intervals {
		if len(res) == 0 || interval[0] > res[len(res)-1][1] {
			// [[1,3],[2,6],[8,10],[15,18]]
			res = append(res, interval)
		} else {
			last := res[len(res)-1]
			res[len(res)-1] = []int{
				last[0], // always unchanged
				int(math.Max(float64(last[1]), float64(interval[1]))),
			}
		}
	}

	return res
}

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	res := [][]int{}

	for _, interval := range intervals {
		if len(res) == 0 || interval[0] > res[len(res)-1][1] {
			// [[1,3],[2,6],[8,10],[15,18]]
			res = append(res, interval)
		} else {
			last := res[len(res)-1]
			res[len(res)-1] = []int{
				int(math.Min(float64(last[0]), float64(interval[0]))),
				int(math.Max(float64(last[1]), float64(interval[1]))),
			}
		}
	}

	return res
}
