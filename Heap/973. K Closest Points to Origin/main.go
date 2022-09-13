// https://leetcode.com/problems/k-closest-points-to-origin/
package main

import (
	"container/heap"
	"math"
)

// T:O(n) average, worst in O(n^2) if array is sorted
// https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.
func kClosestQuickSelect(points [][]int, k int) [][]int {
	target := len(points) - k

	var quickselect func(l, r int) [][]int
	quickselect = func(l, r int) [][]int {
		pivot := points[r]
		pivotDst := distance(pivot)
		p := l
		for i := l; i < r; i++ {
			if distance(points[i]) > pivotDst {
				points[i], points[p] = points[p], points[i]
				p += 1
			}
		}
		points[p], points[r] = points[r], points[p]

		if p == target {
			return points[p:]
		} else if p < target {
			return quickselect(p+1, r)
		} else {
			return quickselect(l, p-1)
		}
	}

	return quickselect(0, len(points)-1)
}

func distance(point []int) int {
	x, y := point[0], point[1]
	return x*x + y*y
}

// T:O(n*logk)
// https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.
// Pros: it can deal with real-time(online) stream data. It does not have to know the size of the data previously.
// Cons: it is not the most efficient solution
func kClosestMaxHeap(points [][]int, k int) [][]int {
	h := MaxHeap([][]int{})

	// n*logk
	for _, point := range points {
		heap.Push(&h, point)
		if h.Len() > k {
			heap.Pop(&h)
		}
	}

	return h
}

// T:O(k*logn)
func kClosest(points [][]int, k int) [][]int {
	h := TupleInt(points)
	heap.Init(&h)

	result := [][]int{}
	for i := 0; i < k; i++ {
		item := heap.Pop(&h)
		result = append(result, item.([]int))
	}

	return result
}

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

func (h *TupleInt) Push(x interface{}) {
	*h = append(*h, x.([]int))
}

func (h *TupleInt) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type MaxHeap [][]int

func (h MaxHeap) Len() int {
	return len(h)
}

func (h MaxHeap) Less(i, j int) bool {
	xi, yi := h[i][0], h[i][1]
	di := math.Pow(float64(xi), 2) + math.Pow(float64(yi), 2)
	// di := math.Sqrt(math.Pow(float64(xi), 2) + math.Pow(float64(yi), 2))

	xj, yj := h[j][0], h[j][1]
	dj := math.Pow(float64(xj), 2) + math.Pow(float64(yj), 2)
	// dj := math.Sqrt(math.Pow(float64(xj), 2) + math.Pow(float64(yj), 2))
	return di > dj
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
