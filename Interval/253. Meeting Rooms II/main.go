// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/meeting-rooms-ii/
package main

import (
	"container/heap"
	"math"
	"sort"
)

// Example 1:
// Input:
// [[0, 30],[5, 10],[15, 20]]
// Output: 2
// Explanation: we need two rooms
// room1:[0,30]
// room2:[5,10],[15,20]

// Example 2:
// Input: [[7,10],[2,4]]
// Output: 1

// [[0, 30],[5, 10],[10, 15]]
// Output: 2
// Explanation: we need two rooms
// room1:[0,30]
// room2:[5,10],[10,15]

// Explanation: https://www.youtube.com/watch?v=FdzJmTCVyJU
// T:O(nLog(n)) M:O(n)
func MeetingRoom2Solution(intervals [][]int) int {
	start, end := []int{}, []int{}
	for _, interval := range intervals {
		start = append(start, interval[0])
		end = append(end, interval[1])
	}
	sort.Ints(start)
	sort.Ints(end)

	res, count := 0, 0
	ptrS, ptrE := 0, 0

	for ptrS < len(intervals) {
		if start[ptrS] < end[ptrE] {
			ptrS += 1
			count += 1
		} else {
			ptrE += 1
			count -= 1
		}
		res = int(math.Max(float64(res), float64(count)))
	}
	return res
}

type MinHeap [][]int

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
	item := old[:length-1]
	*h = old[:length-1]
	return item
}

// not sure if we can pass all the test cases,
// but I think it's correct
func MeetingRoom2(intervals [][]int) int {
	if len(intervals) == 0 {
		return 0
	}

	// T:O(nLog(n)) M:O(n)
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	minRoom := 1

	minEndH := MinHeap([][]int{intervals[0]})
	heap.Init(&minEndH)

	for i := 1; i < len(intervals); i++ {
		interval := intervals[i]
		if interval[0] >= minEndH[0][1] {
			for minEndH.Len() > 0 && interval[0] >= minEndH[0][1] {
				heap.Pop(&minEndH)
			}
		}

		heap.Push(&minEndH, interval)
		minRoom = int(math.Max(float64(minRoom), float64(minEndH.Len())))
	}

	return minRoom
}
