// https://leetcode.com/problems/swim-in-rising-water/

package main

import (
	"container/heap"
	"fmt"
	"math"
)

type Cell struct {
	i, j   int
	weight int
}

/*
Dijkstra
Time for visiting all vertices =O(V+E)
Time required for processing one vertex=O(logV)
Time required for visiting and processing all the vertices = O(V+E)*O(logV) =
*/

// Runtime: 141 ms, faster than 5.09% of Go online submissions for Swim in Rising Water.
// Memory Usage: 7.8 MB, less than 5.09% of Go online submissions for Swim in Rising Water.
// T:O(n^2*log(n^2)) = O(n^2 * (2lg(n))) = O(n^2 * lg(n))
// M:O(n^2)
func swimInWater(grid [][]int) int {
	graph := map[string][]Cell{} // [dst, weight]
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if i+1 < len(grid) {
				graph[key(i, j)] = append(graph[key(i, j)], Cell{i: i + 1, j: j, weight: grid[i+1][j]})
			}
			if i-1 >= 0 {
				graph[key(i, j)] = append(graph[key(i, j)], Cell{i: i - 1, j: j, weight: grid[i-1][j]})
			}
			if j+1 < len(grid[0]) {
				graph[key(i, j)] = append(graph[key(i, j)], Cell{i: i, j: j + 1, weight: grid[i][j+1]})
			}
			if j-1 >= 0 {
				graph[key(i, j)] = append(graph[key(i, j)], Cell{i: i, j: j - 1, weight: grid[i][j-1]})
			}
		}
	}

	minH := MinHeap([]Cell{{i: 0, j: 0, weight: grid[0][0]}})
	visited := map[string]bool{}

	time := 0
	for minH.Len() > 0 {
		src := heap.Pop(&minH).(Cell)

		k := key(src.i, src.j)
		if _, ok := visited[k]; ok {
			continue
		}

		visited[k] = true
		time = int(math.Max(float64(time), float64(src.weight)))
		if src.i == len(grid)-1 && src.j == len(grid[0])-1 {
			break
		}

		for _, neighbor := range graph[k] {
			if _, ok := visited[key(neighbor.i, neighbor.j)]; !ok {
				heap.Push(&minH, neighbor)
			}
		}
	}

	return time
}

// stepwise BFS, inspired by 6ms solution below
func swimInWaterBFSOptimized(grid [][]int) int {
	minH := MinHeap([]Cell{{i: 0, j: 0, weight: grid[0][0]}})
	visited := map[string]bool{}

	time := 0
	for minH.Len() > 0 {
		src := heap.Pop(&minH).(Cell)

		k := key(src.i, src.j)
		if _, ok := visited[k]; ok {
			continue
		}

		visited[k] = true
		time = int(math.Max(float64(time), float64(src.weight)))
		if src.i == len(grid)-1 && src.j == len(grid[0])-1 {
			break
		}

		var directions = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
		for _, dir := range directions {
			x, y := src.i+dir[0], src.j+dir[1]
			xInBounds := x >= 0 && x < len(grid)
			yInBounds := y >= 0 && y < len(grid[0])
			if xInBounds && yInBounds && !visited[key(x, y)] {
				heap.Push(&minH, Cell{x, y, grid[x][y]})
			}
		}
	}

	return time
}

func key(i, j int) string {
	return fmt.Sprintf("%d,%d", i, j)
}

// 6 ms submission
// stepwise search
func swimInWaterOptimizedDFS(grid [][]int) int {
	n := len(grid)
	visited := map[int]bool{}
	var time int

	h := new(MinHeap)
	heap.Push(h, Cell{0, 0, grid[0][0]})

	var dfs func(a, b int) bool
	dfs = func(a, b int) bool {
		if a == n-1 && b == n-1 {
			return true
		}
		visited[grid[a][b]] = true

		var directions = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
		for _, dir := range directions {
			x, y := a+dir[0], b+dir[1]

			xInBounds := x >= 0 && x < n
			yInBounds := y >= 0 && y < n
			if xInBounds && yInBounds && !visited[grid[x][y]] {
				if weight := grid[x][y]; weight <= time {
					if dfs(x, y) {
						return true
					}
				} else {
					heap.Push(h, Cell{x, y, weight})
				}
			}
		}
		return false
	}

	for {
		cell := heap.Pop(h).(Cell)
		time = cell.weight

		if dfs(cell.i, cell.j) {
			return time
		}
	}
}

type MinHeap []Cell

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	return h[i].weight < h[j].weight
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.(Cell))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
