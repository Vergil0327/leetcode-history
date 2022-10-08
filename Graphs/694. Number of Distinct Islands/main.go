package main

import "fmt"

// use relative coordinate to distinguish
func numDistinctIslands(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(state *string, r0, c0, r, c int)
	dfs = func(state *string, r0, c0, r, c int) {
		if grid[r][c] != 1 {
			return
		}

		*state += fmt.Sprintf("[%d,%d]", r-r0, c-c0)
		grid[r][c] *= -1 // mark visited

		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]
			row, col := r+dr, c+dc
			rowInBounds, colInBounds := row >= 0 && row < ROWS, col >= 0 && col < COLS
			if rowInBounds && colInBounds {
				dfs(state, r0, c0, row, col)
			}
		}
	}

	res := map[string]struct{}{}
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if grid[r][c] != 1 {
				continue
			}

			state := ""
			dfs(&state, r, c, r, c)
			res[state] = struct{}{}
		}
	}

	return len(res)
}
