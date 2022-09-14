// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/
package main

import "container/heap"

// ! we can solve this simply by sliding window with two deque in time complexity T:O(n)
// see: ../../Sliding Window/1438.

// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)
// T:O(nLogn) M:O(n)
func longestSubarray(nums []int, limit int) int {
	// [value, index]
	maxH := MaxHeap([][]int{})
	minH := MinHeap([][]int{})
	l := 0
	maxLen := 0
	for r, num := range nums {
		heap.Push(&maxH, []int{num, r})
		heap.Push(&minH, []int{num, r})

		for maxH[0][0]-minH[0][0] > limit {
			l = Min(maxH[0][1], minH[0][1]) + 1

			// pop until valid
			for maxH[0][1] < l {
				heap.Pop(&maxH)
			}
			for minH[0][1] < l {
				heap.Pop(&minH)
			}
		}
		maxLen = Max(maxLen, r-l+1)
	}

	return maxLen
}

func Min(a, b int) int {
	if a <= b {
		return a
	}

	return b
}
func Max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}

type MaxHeap [][]int // [value, index]
func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Less(i, j int) bool {
	return h[i][0] > h[j][0]
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

type MinHeap [][]int

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	return h[i][0] < h[j][0]
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
