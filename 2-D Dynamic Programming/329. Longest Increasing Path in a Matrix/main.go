// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

package main

import (
	"fmt"
	"math"
)

// https://www.youtube.com/watch?v=wCc_nd-GiEc
// T:O(m*n) M:O(m*n)
func longestIncreasingPathOptimized(matrix [][]int) int {
	ROW, COL := len(matrix), len(matrix[0])
	memo := map[string]int{}

	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(i, j, prev int) int
	dfs = func(i, j, prev int) int {
		iInBounds := i >= 0 && i < ROW
		jInBounds := j >= 0 && j < COL
		if !iInBounds || !jInBounds || matrix[i][j] <= prev {
			return 0
		}

		key := fmt.Sprintf("%d,%d", i, j)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		for _, dir := range directions {
			x, y := i+dir[0], j+dir[1]

			memo[key] = int(math.Max(float64(memo[key]), float64(1+dfs(x, y, matrix[i][j]))))
		}

		return memo[key]
	}

	max := 0
	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			max = int(math.Max(float64(max), float64(dfs(i, j, -1))))
		}
	}

	return max
}

// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/288520/Longest-Path-in-DAG
// We regard
//   - a cell in the matrix as a node,
//   - a directed edge from node x to node y if x and y are adjacent and x's value < y's value
//
// Then a graph is formed.
// No cycles can exist in the graph, i.e. a DAG is formed.
// The problem becomes to get the longest path in the DAG.
// Topological sort can iterate the vertices of a DAG in the linear ordering.
// Using Kahn's algorithm(BFS) to implement topological sort while counting the levels can give us the longest chain of nodes in the DAG.
// T:O(E+V) M:O(m*n)
// https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
func longestIncreasingPathTopoligicalSort(matrix [][]int) int {
	ROW, COL := len(matrix), len(matrix[0])

	if ROW == 0 {
		return 0
	}

	inDegrees := make([][]int, ROW)
	for i := range inDegrees {
		inDegrees[i] = make([]int, COL)
	}

	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for r := 0; r < ROW; r++ {
		for c := 0; c < COL; c++ {
			for _, dir := range directions {
				x, y := r+dir[0], c+dir[1]
				xInBounds := x >= 0 && x < ROW
				yInBounds := y >= 0 && y < COL
				// SMALLER       LARGER
				// node(i,j) --> node(nx,ny)
				if xInBounds && yInBounds && matrix[x][y] > matrix[r][c] {
					inDegrees[x][y] += 1
				}
			}
		}
	}

	queue := [][]int{}
	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			if inDegrees[i][j] == 0 {
				queue = append(queue, []int{i, j})
			}
		}
	}

	LIP := 0
	for len(queue) > 0 {
		for _, cord := range queue {
			queue = queue[1:]
			i, j := cord[0], cord[1]

			for _, dir := range directions {
				x, y := i+dir[0], j+dir[1]
				xInBounds := x >= 0 && x < ROW
				yInBounds := y >= 0 && y < COL
				if xInBounds && yInBounds && matrix[x][y] > matrix[i][j] {
					inDegrees[x][y] -= 1
					if inDegrees[x][y] == 0 {
						queue = append(queue, []int{x, y})
					}
				}
			}
		}
		LIP += 1
	}

	return LIP
}

func longestIncreasingPathSlow(matrix [][]int) int {
	ROW, COL := len(matrix), len(matrix[0])
	memo := map[string]int{}

	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(i, j, prev int) int
	dfs = func(i, j, prev int) int {
		iInBounds := i >= 0 && i < ROW
		jInBounds := j >= 0 && j < COL
		if !iInBounds || !jInBounds || matrix[i][j] <= prev {
			return 0
		}

		// we don't need to cache prev actually, because we'll choose max value from 4 direction as current longest increasing path(LIP).
		// it doesn't change cached LIP value by different prev
		key := fmt.Sprintf("%d,%d,%d", i, j, prev)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		for _, dir := range directions {
			x, y := i+dir[0], j+dir[1]

			memo[key] = int(math.Max(float64(memo[key]), float64(1+dfs(x, y, matrix[i][j]))))
		}

		return memo[key]
	}

	max := 0
	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			max = int(math.Max(float64(max), float64(dfs(i, j, -1))))
		}
	}

	return max
}
