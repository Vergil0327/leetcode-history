// https://leetcode.com/problems/max-area-of-island/
package main

import "fmt"

// Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
// 								[0,0,0,0,0,0,0,1,1,1,0,0,0],
// 								[0,1,1,0,1,0,0,0,0,0,0,0,0],
// 								[0,1,0,0,1,1,0,0,1,0,1,0,0],
// 								[0,1,0,0,1,1,0,0,1,1,1,0,0],
// 								[0,0,0,0,0,0,0,0,0,0,1,0,0],
// 								[0,0,0,0,0,0,0,1,1,1,0,0,0],
// 								[0,0,0,0,0,0,0,1,1,0,0,0,0]]
// Output: 6
// Explanation: The answer is not 11, because the island must be connected 4-directionally.
type any = interface{}

const WATER int = 0
const LAND int = 1

// explnation: https://www.youtube.com/watch?v=iJGr1OtmH0c
// freecodecamp: https://www.youtube.com/watch?v=tWVWeAqZ0WU
func maxAreaOfIsland(grid [][]int) int {
	max := 0
	visited := map[string]any{}
	for row := 0; row < len(grid); row++ {
		for col := 0; col < len(grid[0]); col++ {
			if grid[row][col] == WATER {
				continue
			}
			key := fmt.Sprintf("%d,%d", row, col)
			if _, ok := visited[key]; ok {
				continue
			}

			tmp := explore(grid, row, col, visited)
			if tmp > max {
				max = tmp
			}
		}
	}

	return max
}

func explore(grid [][]int, r, c int, visited map[string]any) int {
	rowInBounds := r >= 0 && r < len(grid)
	colInBounds := c >= 0 && c < len(grid[0])
	if !rowInBounds || !colInBounds {
		return 0
	}

	if grid[r][c] == WATER {
		return 0
	}

	key := fmt.Sprintf("%d,%d", r, c)
	if _, ok := visited[key]; ok {
		return 0
	}

	visited[key] = struct{}{}
	return 1 +
		explore(grid, r+1, c, visited) +
		explore(grid, r-1, c, visited) +
		explore(grid, r, c+1, visited) +
		explore(grid, r, c-1, visited)
}
