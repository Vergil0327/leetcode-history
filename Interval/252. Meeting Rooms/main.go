package main

import (
	"sort"
)

// T: O(n)
// [[0,30],[5,10],[15,20]], false
// [[7,10],[2,4]], true
func SolutionsWithWithoutSorting(intervals [][2]int) bool {
	for i := 0; i < len(intervals); i++ {
		for j := i + 1; j < len(intervals); j++ {
			if curr, next := intervals[i], intervals[j]; next[0] >= curr[0] && next[1] <= curr[1] {
				return false
			}
		}
	}

	return true
}

func SolutionsWithSorting(intervals [][2]int) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for i := 0; i < len(intervals)-1; i++ {
		if intervals[i+1][1] < intervals[0][1] {
			return false
		}
	}

	return true
}
