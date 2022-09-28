package main

import (
	"container/heap"
	"sort"
)

// take from nearest lastDay
// if exceed, pop out largest duration && push current
// keep heap valid
// GREEDY SOLUTION: https://www.youtube.com/watch?v=PTD5SaqqE-w
func scheduleCourse(courses [][]int) int {
	minLastDay := MinHeap(courses)
	heap.Init(&minLastDay)
	curr := MaxHeap([][]int{})

	totalDur := 0
	deadline := 0
	for minLastDay.Len() > 0 {
		crs := heap.Pop(&minLastDay).([]int)

		// filter out impossible course
		dur, las := crs[0], crs[1]
		if dur > las {
			continue
		}

		heap.Push(&curr, crs)
		totalDur += dur
		deadline = las

		if totalDur > deadline {
			pop := heap.Pop(&curr).([]int)
			totalDur -= pop[0]
		}
	}

	return curr.Len()
}

// Time: nlon(n), Memory: O(n)
func scheduleCourseOptimized(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		return courses[i][1] < courses[j][1]
	})

	maxDur := MaxHeap([][]int{})
	time := 0

	for _, crs := range courses {
		if time+crs[0] <= crs[1] {
			time += crs[0]
			heap.Push(&maxDur, crs)
		} else if maxDur.Len() > 0 && maxDur[0][0] > crs[0] {
			time += crs[0] - heap.Pop(&maxDur).([]int)[0]
			heap.Push(&maxDur, crs)
		}
	}

	return maxDur.Len()
}

type MinHeap [][]int // min(lastDay), [duration, lastDay]

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	if h[i][1] == h[j][1] { // tie breaker, if equal, return smaller duration
		return h[i][0] < h[j][0]
	}
	return h[i][1] < h[j][1]
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

type any = interface{}

func (h *MinHeap) Push(item any) {
	*h = append(*h, item.([]int))
}
func (h *MinHeap) Pop() any {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type MaxHeap [][]int // max(duration), [duration, lastDay]

func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Less(i, j int) bool {
	if h[i][0] == h[j][0] {
		return h[i][1] < h[j][1]
	}
	return h[i][0] > h[j][0]
}
func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MaxHeap) Push(item any) {
	*h = append(*h, item.([]int))
}
func (h *MaxHeap) Pop() any {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
