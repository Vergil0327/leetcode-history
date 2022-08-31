package main

import "container/heap"

// Less(i, j int) bool
// Swap(i, j int)
// Push(x any) // add x as element Len()
// Pop() any   // remove and return element Len() - 1.
type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}
func (h IntHeap) Less(i, j int) bool {
	return h[i] > h[j]
}
func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// T: O(nLogN)
func lastStoneWeight(stones []int) int {
	h := IntHeap(stones)
	heap.Init(&h)

	// N
	for len(h) > 1 {
		x := heap.Pop(&h).(int)
		y := heap.Pop(&h).(int)
		if val := x - y; val > 0 {
			heap.Push(&h, val) // O(logN)
		}
	}

	if len(h) > 0 {
		return h[0]
	}

	return 0
}
