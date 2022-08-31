// https://leetcode.com/problems/insert-interval/

package main

import "math"

// T:O(n) M:O(n)
func insert(intervals [][]int, newInterval []int) [][]int {
	res := [][]int{newInterval}

	for _, interval := range intervals {
		start, end := interval[0], interval[1]

		if end < res[len(res)-1][0] {
			// think this case: [[2,6],[7,9]], [15,18]
			last := res[len(res)-1]
			res[len(res)-1] = interval
			res = append(res, last)
		} else if start > res[len(res)-1][1] {
			res = append(res, interval)
		} else {
			res[len(res)-1][0] = int(math.Min(float64(res[len(res)-1][0]), float64(start)))
			res[len(res)-1][1] = int(math.Max(float64(res[len(res)-1][1]), float64(end)))
		}
	}

	return res
}

// explanation: https://www.youtube.com/watch?v=A8NUOmlwOlM
func insertNeetCode(intervals [][]int, newInterval []int) [][]int {
	res := [][]int{}
	for i, interval := range intervals {
		if newInterval[1] > interval[0] {
			res = append(res, newInterval)
			return append(res, intervals[i:]...)
		} else if newInterval[0] > interval[1] {
			res = append(res, interval)
		} else {
			newInterval = []int{
				int(math.Min(float64(newInterval[0]), float64(interval[0]))),
				int(math.Max(float64(newInterval[1]), float64(interval[1]))),
			}
		}
	}

	res = append(res, newInterval)
	return res
}
