// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
package main

import "container/heap"

// https://www.youtube.com/watch?v=JJUv4DDLSB4
// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
// The key point for any binary search is to figure out the "Search Space". For me, I think there are two kind of "Search Space" -- index and range(the range from the smallest number to the biggest number). Most usually, when the array is sorted in one direction, we can use index as "search space", when the array is unsorted and we are going to find a specific number, we can use "range".
// The reason why we did not use index as "search space" for this problem is the matrix is sorted in two directions, we can not find a linear way to map the number and its index.
// T:O(nlogn) M:O(1)
func kthSmallestBinarySearch(matrix [][]int, k int) int {
	// use value range as search space
	N := len(matrix)

	// start from bottom-left to top-right:
	// 	if element > target: move up and right half are greater than target
	// 	if element <= target: move right and all above the elements are smaller than target
	var countSmallerOrEqual func(val int) int = func(val int) int {
		r, c := N-1, 0
		count := 0
		for r >= 0 && c < N {
			if matrix[r][c] <= val {
				count += r + 1 // plus 1 because of 0-based index offset
				c += 1
			} else {
				r -= 1
			}
		}

		return count
	}

	// we want to find the minumun value satisfied the condition `countSmallerOrEqual(mid) >= k`
	// i.e. find uppper limit
	lo, hi := matrix[0][0], matrix[N-1][N-1]+1
	for lo < hi {
		mid := lo + (hi-lo)/2
		count := countSmallerOrEqual(mid) // # of elements <= mid
		if count < k {
			lo = mid + 1
		} else /* countSmallerOrEqual(mid) >= k */ {
			hi = mid
		}
	}

	return lo
}

// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
// we know that elements are sorted in either row or column
// top-left is smallest & bottom-right is largest,
// so we can find kth smallest from top to bottom with min heap
// klog(#row)
func kthSmallestOptimized(matrix [][]int, k int) int {
	N := len(matrix) // n * n matrix
	h := MinHeap([]Tuple{})

	// push elements in first row and search from top to bottom
	for c := 0; c < N; c++ {
		heap.Push(&h, Tuple{0, c, matrix[0][c]})
	}

	// find kth smallest from top to bottom
	// pop first k-1 small element
	for i := 0; i < k-1; i++ {
		tup := heap.Pop(&h).(Tuple)
		r, c := tup[0], tup[1]
		if r == N-1 {
			continue
		}
		heap.Push(&h, Tuple{r + 1, c, matrix[r+1][c]})
	}

	return h[0][2]
}

type Tuple []int // [row, col, val]
type MinHeap []Tuple

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	return h[i][2] < h[j][2]
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.(Tuple))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

// T:O(nlogk) M:O(k)
// pop out larger than kth
func kthSmallest(matrix [][]int, k int) int {
	ROWS, COLS := len(matrix), len(matrix[0])

	h := MaxHeap([]int{})
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			heap.Push(&h, matrix[r][c])
			if h.Len() > k {
				heap.Pop(&h)
			}
		}
	}

	return h[0]
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
