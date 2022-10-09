package main

import "container/heap"

// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/discuss/2678850/Lexicographical-smallest-oror-One-Pass
func hardestWorkerOnePass(n int, logs [][]int) int {
	id := logs[0][0]
	workTime := logs[0][1]
	for i := 1; i < len(logs); i++ {
		workerID := logs[i][0]
		currWorkTime := logs[i][1] - logs[i-1][1]

		if currWorkTime > workTime || (currWorkTime == workTime && workerID < id) {
			workTime = currWorkTime
			id = workerID
		}
	}

	return id
}

func hardestWorker(n int, logs [][]int) int {
	maxH := MaxHeap([][]int{}) // [id, duration]
	currTime := 0
	for _, log := range logs {
		maxH = append(maxH, []int{log[0], log[1] - currTime})
		currTime = log[1]
	}

	heap.Init(&maxH)
	return maxH[0][0]
}

type MaxHeap [][]int // [id, duration]

func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Less(i, j int) bool {
	if h[i][1] == h[j][1] {
		return h[i][0] < h[j][0]
	}
	return h[i][1] > h[j][1]
}
func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.([]int))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
