// https://leetcode.com/problems/non-overlapping-intervals/
package main

import (
	"math"
	"sort"
)

/*
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
*/

// [[1,2],[1,2],[1,2]]
// [[1,2],[2,3],[3,4],[1,3]]
// [[1,100],[11,22],[1,11],[2,12]]
// [[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]
// [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
// Expected: 2
// Expected: 1
// Expected: 2
// Expected: 4
// Expected: 7
// after sorting:
// [[1 2] [1 2] [1 2]]
// [[1 2] [1 3] [2 3] [3 4]]
// [[1 11] [1 100] [2 12] [11 22]]
// [[0 2] [1 3] [1 3] [2 4] [3 5] [3 5] [4 6]]
// [[-73 -26] [-65 -11] [-63 2] [-62 -49] [-52 31] [-40 -26] [-31 49] [30 47] [58 95] [66 98] [82 97] [95 99]]

// Explanation: https://www.youtube.com/watch?v=nONCGxWoUfM
// T:O(nLog(n)) because of sorting
func eraseOverlapIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	count := 0
	prevEnd := intervals[0][1] // tracking previous valid end & be greedy
	for i := 1; i < len(intervals); i++ {
		start, end := intervals[i][0], intervals[i][1]
		if start >= prevEnd {
			prevEnd = end // update current valid end
		} else {
			count += 1
			prevEnd = int(math.Min(float64(prevEnd), float64(end))) // remove the most small one, (BE GREEDY), because it'll be less chance to overlap next interval
		}
	}

	return count
}
