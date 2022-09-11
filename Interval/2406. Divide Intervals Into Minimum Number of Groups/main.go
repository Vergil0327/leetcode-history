// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
package main

import (
	"container/heap"
	"sort"
)

/*
Input: intervals = [[1,5],[1,10],[2,3],[5,10],[6,8]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
*/

// T:O(nLogn)
func minGroups(intervals [][]int) int {
	sort.Slice(intervals, func(i int, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})

	h := MinHeap([][]int{})
	for _, interval := range intervals {
		start := interval[0]

		if h.Len() == 0 {
			heap.Push(&h, interval)
		} else {
			if start <= h[0][1] {
				heap.Push(&h, interval)
			} else {
				heap.Pop(&h)
				heap.Push(&h, interval)
			}
		}
	}

	return h.Len()
}

type MinHeap [][]int // sort end time ascendingly

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	return h[i][1] < h[j][1]
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.([]int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

func minGroupsTimeout(intervals [][]int) int {
	sort.Slice(intervals, func(i int, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})

	group := []int{}
LOOP:
	for _, interval := range intervals {
		start, end := interval[0], interval[1]
		if len(group) == 0 {
			group = append(group, end)
		} else {
			sort.Ints(group)
			for i, g := range group {
				if start > g {
					group[i] = end
					continue LOOP
				}
			}
			group = append(group, end)
		}
	}

	return len(group)
}
