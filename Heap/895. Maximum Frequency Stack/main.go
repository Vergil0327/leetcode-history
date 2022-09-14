// https://leetcode.com/problems/maximum-frequency-stack/

package main

import "container/heap"

// push val onto top of stack
// freq += 1 -> hashmap
// push to max heap [val, freq]
// if contains [val, freq], [val, freq+1], ...
// we can still pop most frequent and keep less frequent one exists in FreqStack
type FreqStack struct {
	index   int
	freq    map[int]int
	maxHeap MaxHeap
}

func Constructor() FreqStack {
	return FreqStack{freq: make(map[int]int), maxHeap: MaxHeap([][]int{})}
}

// T:O(nlogn)
func (this *FreqStack) Push(val int) {
	this.freq[val] += 1
	this.index += 1
	heap.Push(&this.maxHeap, []int{val, this.freq[val], this.index})
}

// T:O(nlogn)
func (this *FreqStack) Pop() int {
	item := heap.Pop(&this.maxHeap).([]int) // [val, freq, index]
	this.freq[item[0]] -= 1
	return item[0]
}

type MaxHeap [][]int // [val, freq, index]

func (h MaxHeap) Len() int {
	return len(h)
}

// If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
// tie-breaker: increasing index
func (h MaxHeap) Less(i, j int) bool {
	if h[i][1] == h[j][1] {
		return h[i][2] > h[j][2]
	}
	return h[i][1] > h[j][1]
}

func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MaxHeap) Push(item interface{}) {
	*h = append(*h, item.([]int))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
