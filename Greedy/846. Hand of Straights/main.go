// https://leetcode.com/problems/hand-of-straights/
package main

import "container/heap"

/*
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8] */
// solution: https://www.youtube.com/watch?v=amnrMCVd2YI
type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}
func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
func (h *IntHeap) Push(item interface{}) {
	*h = append(*h, item.(int))
}

func isNStraightHand(hand []int, groupSize int) bool {
	if len(hand)%groupSize != 0 {
		return false
	}

	// 1,2,2,3,3,4,6,7,8
	cntMap := map[int]int{}
	for _, card := range hand {
		cntMap[card] += 1
	}

	keys := []int{}
	for k := range cntMap {
		keys = append(keys, k)
	}
	h := IntHeap(keys) // we don't want duplicate, because we want to track first card of straight group
	heap.Init(&h)

	for h.Len() > 0 {
		first := h[0]
		for i := first; i < first+groupSize; i++ {
			// we don't have card to complete the straight
			if _, ok := cntMap[i]; !ok {
				return false
			}

			cntMap[i] -= 1
			if cntMap[i] == 0 {
				card := heap.Pop(&h).(int)
				if card != i {
					return false // because we can't complete next group of straight
				}
			}
		}
	}

	return true
}
