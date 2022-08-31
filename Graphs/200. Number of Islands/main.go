// https://leetcode.com/problems/number-of-islands/
package main

import "fmt"

/*
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
*/

const WATER = byte('0')
const LAND = byte('1')

// explanation: https://www.youtube.com/watch?v=pV2kpPD66nE
// freecodecamp tutorial of graph: https://www.youtube.com/watch?v=tWVWeAqZ0WU
func numIslands(grid [][]byte) int {
	visited := map[string]bool{}
	num := 0

	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			if grid[r][c] == WATER {
				continue
			}

			key := fmt.Sprintf("%d,%d", r, c)
			if visited[key] {
				continue
			}

			if dfs(grid, r, c, visited) {
				num += 1
			}
		}
	}

	return num
}

func dfs(grid [][]byte, r, c int, visited map[string]bool) bool {
	rowInBounds := r >= 0 && r < len(grid)
	colInBounds := c >= 0 && c < len(grid[0])
	if !rowInBounds || !colInBounds {
		return false
	}

	key := fmt.Sprintf("%d,%d", r, c)
	if visited[key] {
		return false
	}

	if grid[r][c] == WATER {
		return false
	}

	visited[key] = true

	// explore all directions, mark visited if needed
	dfs(grid, r+1, c, visited)
	dfs(grid, r-1, c, visited)
	dfs(grid, r, c+1, visited)
	dfs(grid, r, c-1, visited)

	return true
}
