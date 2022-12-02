// https://leetcode.com/problems/network-delay-time/
package main

import (
	"container/heap"
	"math"
)

// times[i] = (ui, vi, wi),
// ui is the source node
// vi is the target node
// wi is the time it takes for a signal to travel from source to target.
// Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
// Expected: 2
// ! test if you know the Dijkstra's algorithm
func networkDelayTime(times [][]int, n int, k int) int {
	adj := make(map[int][][]int, n)
	for _, node := range times {
		u, v, w := node[0], node[1], node[2]
		if _, ok := adj[u]; !ok {
			adj[u] = make([][]int, 0)
		}
		adj[u] = append(adj[u], []int{v, w}) // [node, weight]
	}

	visited := map[int]bool{}
	minH := MinHeap([][]int{{k, 0}})
	time := 0
	for len(minH) > 0 {
		item := heap.Pop(&minH).([]int)
		v, w := item[0], item[1]
		if visited[v] {
			continue
		}

		visited[v] = true
		time = int(math.Max(float64(time), float64(w)))
		for _, neighbor := range adj[v] {
			v2, w2 := neighbor[0], neighbor[1]
			if !visited[v2] {
				heap.Push(&minH, []int{v2, w + w2})
			}
		}
	}

	if len(visited) == n /* traversal all the node */ {
		return time
	} else {
		return -1
	}
}

type MinHeap [][]int // [[node, weight]...]

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	return h[i][1] < h[j][1]
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.([]int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
