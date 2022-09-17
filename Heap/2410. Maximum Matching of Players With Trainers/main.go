// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
package main

import (
	"container/heap"
	"sort"
)

// sorting & greedy & two-pointers
// nlogn
func matchPlayersAndTrainersSorting(players []int, trainers []int) int {
	sort.Ints(players)
	sort.Ints(trainers)

	p, t := 0, 0
	count := 0
	for p < len(players) && t < len(trainers) {
		if players[p] <= trainers[t] {
			p, t = p+1, t+1
			count += 1
		} else {
			t += 1
		}
	}
	return count
}

// nlogn
func matchPlayersAndTrainers(players []int, trainers []int) int {
	sort.Ints(players)
	h := MaxHeap(trainers)
	heap.Init(&h)

	count := 0
	for i := len(players) - 1; i >= 0; i-- {
		if players[i] <= h[0] {
			heap.Pop(&h)
			count += 1
		}
		if h.Len() == 0 {
			break
		}
	}

	return count
}

type MaxHeap []int

func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Less(i, j int) bool {
	return h[i] > h[j]
}
func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
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
