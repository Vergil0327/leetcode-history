// https://leetcode.com/problems/min-cost-to-connect-all-points/
package main

import (
	"container/heap"
	"math"
)

type MinHeapEdge [][]int

func (h MinHeapEdge) Len() int {
	return len(h)
}
func (h MinHeapEdge) Less(i, j int) bool {
	return h[i][0] < h[j][0]
}
func (h MinHeapEdge) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeapEdge) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
func (h *MinHeapEdge) Push(x interface{}) {
	*h = append(*h, x.([]int))
}

// Minimum Spanning Tree (MST)
// use Prim's algorithm
// explanation: https://www.youtube.com/watch?v=f7JOBJIC-NA
// T:O(n^2log(n)), n^2 for all the number of edges & log(n) for Prim's algorithm by min heap implementation
func minCostConnectPoints(points [][]int) int {
	// edge preparation
	adjacencyList := make(map[int][][]int, len(points)) // i-th point: list of [weight, node]

	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			dst := manhattanDistance(points[i], points[j])
			if _, ok := adjacencyList[i]; !ok {
				adjacencyList[i] = make([][]int, 0)
			}
			if _, ok := adjacencyList[j]; !ok {
				adjacencyList[j] = make([][]int, 0)
			}

			// undirected graph
			adjacencyList[i] = append(adjacencyList[i], []int{int(dst), j})
			adjacencyList[j] = append(adjacencyList[j], []int{int(dst), i})
		}
	}

	// Prim's algorithm implementation
	result := 0
	visited := map[int]bool{}
	minH := MinHeapEdge([][]int{{0, 0}}) // [cost, i-th point]

	for len(visited) < len(points) {
		item := heap.Pop(&minH).([]int)
		cost, i := item[0], item[1]
		if visited[i] {
			continue
		}

		visited[i] = true
		result += cost
		for _, neighbor := range adjacencyList[i] {
			neiCost, j := neighbor[0], neighbor[1]
			if !visited[j] {
				heap.Push(&minH, []int{neiCost, j})
			}
		}
	}

	return result
}

func manhattanDistance(point1, point2 []int) float64 {
	x1, y1 := point1[0], point1[1]
	x2, y2 := point2[0], point2[1]
	return math.Abs(float64(x2-x1)) + math.Abs(float64(y2-y1))
}
