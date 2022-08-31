// https://leetcode.com/problems/k-closest-points-to-origin/
package main

import (
	"container/heap"
	"math"
)

// Input: points = [[1,3],[-2,2]], k = 1
// Output: [[-2,2]]
// Explanation:
// The distance between (1, 3) and the origin is sqrt(10).
// The distance between (-2, 2) and the origin is sqrt(8).
// Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
// We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

type TupleInt [][]int

func (h TupleInt) Len() int {
	return len(h)
}

func (h TupleInt) Less(i, j int) bool {
	xi, yi := h[i][0], h[i][1]
	di := math.Pow(float64(xi), 2) + math.Pow(float64(yi), 2)
	// di := math.Sqrt(math.Pow(float64(xi), 2) + math.Pow(float64(yi), 2))

	xj, yj := h[j][0], h[j][1]
	dj := math.Pow(float64(xj), 2) + math.Pow(float64(yj), 2)
	// dj := math.Sqrt(math.Pow(float64(xj), 2) + math.Pow(float64(yj), 2))
	return di < dj
}

func (h TupleInt) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *TupleInt) Push(x any) {
	*h = append(*h, x.([]int))
}

func (h *TupleInt) Pop() any {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

func kClosest(points [][]int, k int) [][]int {
	h := TupleInt(points)
	heap.Init(&h)
	for _, point := range points {
		heap.Push(&h, point)
	}

	result := [][]int{}
	for i := 0; i < k; i++ {
		item := heap.Pop(&h)
		result = append(result, item.([]int))
	}

	return result
}
