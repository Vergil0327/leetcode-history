// https://leetcode.com/problems/find-median-from-data-stream/
package main

import "container/heap"

// explanation: https://www.youtube.com/watch?v=itmhHWaHupI
type MedianFinder struct {
	// small group <= large group
	small MaxHeap
	large MinHeap
}

func Constructor() MedianFinder {
	minH := MinHeap([]int{})
	maxH := MaxHeap([]int{})
	return MedianFinder{small: maxH, large: minH}
}

func (this *MedianFinder) AddNum(num int) {
	heap.Push(&this.small, num)

	if this.small.Len() > 0 && this.large.Len() > 0 && this.small[0] > this.large[0] {
		item := heap.Pop(&this.small)
		heap.Push(&this.large, item)
	}

	if this.small.Len() > this.large.Len()+1 {
		item := heap.Pop(&this.small)
		heap.Push(&this.large, item)
	}

	if this.large.Len() > this.small.Len()+1 {
		item := heap.Pop(&this.large)
		heap.Push(&this.small, item)
	}

}

func (this *MedianFinder) FindMedian() float64 {
	if this.small.Len() > this.large.Len() {
		return float64(this.small[0])
	}

	if this.large.Len() > this.small.Len() {
		return float64(this.large[0])
	}

	return (float64(this.small[0]) + float64(this.large[0])) / 2
}

type MaxHeap []int

func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h MaxHeap) Less(i, j int) bool {
	return h[i] > h[j]
}
func (h *MaxHeap) Push(item interface{}) {
	*h = append(*h, item.(int))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type MinHeap []int

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h MinHeap) Less(i, j int) bool {
	return h[i] < h[j]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.(int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

/**
* Your MedianFinder object will be instantiated and called as such:
* obj := Constructor();
* obj.AddNum(num);
* param_2 := obj.FindMedian();
 */
