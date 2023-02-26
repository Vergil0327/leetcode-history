package leetcode2577

import (
	"container/heap"
)

func minimumTime(grid [][]int) int {
	if grid[0][1] > 1 && grid[1][0] > 1 {
		return -1
	}

	m, n := len(grid), len(grid[0])
	queue := MinHeap([][]int{{0, 0, 0}}) // time, row, col
	visited := map[[2]int]struct{}{{0, 0}: {}}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for queue.Len() > 0 {
		top := heap.Pop(&queue).([]int)
		time, r, c := top[0], top[1], top[2]
		if r == m-1 && c == n-1 {
			return time
		}

		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]
			row, col := r+dr, c+dc
			if row < 0 || row >= m || col < 0 || col >= n {
				continue
			}
			if _, exists := visited[[2]int{row, col}]; exists {
				continue
			}
			visited[[2]int{row, col}] = struct{}{}

			if time+1 >= grid[row][col] {
				heap.Push(&queue, []int{time + 1, row, col})
			} else {
				back_and_forth := grid[row][col] - time
				if back_and_forth%2 == 0 {
					back_and_forth += 1
				}
				heap.Push(&queue, []int{time + back_and_forth, row, col})
			}
		}
	}
	return -1
}

type MinHeap [][]int

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h MinHeap) Less(i, j int) bool {
	return h[i][0] < h[j][0]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.([]int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}
