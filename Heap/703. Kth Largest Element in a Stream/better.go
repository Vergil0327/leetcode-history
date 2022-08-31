package main

import (
	"container/heap"
)

// min heap of size k
// add/pop O(logN) better than O(n) of list insertion
// min value O(1)
type IntHeap []int

// sort.Interface
func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	popItem := old[n-1]
	*h = old[:n-1]
	return popItem
}

type KthLargestBetter struct {
	minHeap IntHeap
	k       int
}

func ConstructorBetter(k int, nums []int) KthLargestBetter {
	h := IntHeap(nums)
	heap.Init(&h)
	for len(h) > k {
		heap.Pop(&h)
	}

	return KthLargestBetter{minHeap: h, k: k}
}

func (this *KthLargestBetter) Add(val int) int {
	heap.Push(&this.minHeap, val)
	if len(this.minHeap) > this.k {
		heap.Pop(&this.minHeap)
	}

	return this.minHeap[0]
}
