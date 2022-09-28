package main

import "math"

// https://www.youtube.com/watch?v=VpEEtzIMOKg&ab_channel=HuaHua
func shortestPath(grid [][]int, k int) int {
	ROWS, COLS := len(grid), len(grid[0])

	memo := map[[2]int]int{} // memo[r,c] = min(k), min obstacle we got when we reach (r,c). the lower k is, the better we get
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			// starting point is guarenteed 0 obstacle
			if r == 0 && c == 0 {
				memo[[2]int{r, c}] = 0
				continue
			}

			memo[[2]int{r, c}] = math.MaxInt
		}
	}

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	queue := [][3]int{{0, 0, 0}} // [row, col, obstacles]
	steps := 0
	for len(queue) > 0 {
		for _, pos := range queue {
			queue = queue[1:]
			r, c, obs := pos[0], pos[1], pos[2]

			if r == ROWS-1 && c == COLS-1 {
				return steps
			}

			for _, dir := range dirs {
				dr, dc := dir[0], dir[1]
				row, col := r+dr, c+dc

				rowInBounds := row >= 0 && row < ROWS
				colInBounds := col >= 0 && col < COLS
				if rowInBounds && colInBounds {
					newObs := obs
					if grid[row][col] == 1 {
						newObs += 1
					}
					// or we can just newObs := obs + grid[row][col]

					// invalid path
					if newObs > k {
						continue
					}

					// same path exists
					if newObs >= memo[[2]int{row, col}] {
						continue
					}

					// memorization, just like Top-Down DP
					memo[[2]int{row, col}] = newObs

					queue = append(queue, [3]int{row, col, newObs})
				}
			}
		}
		steps += 1
	}

	return -1
}

// 1st try, FAILED
func shortestPathTLE(grid [][]int, k int) int {
	ROWS, COLS := len(grid), len(grid[0])

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	var bfs func(i, j, k, currSteps int, visited map[[2]int]bool) int
	bfs = func(i, j, k, currSteps int, visited map[[2]int]bool) int {
		steps := currSteps
		res := math.MaxInt
		queue := [][2]int{{i, j}}
		for len(queue) > 0 {
			for _, pos := range queue {
				queue = queue[1:]

				r, c := pos[0], pos[1]
				if r == ROWS-1 && c == COLS-1 {
					if res != math.MaxInt {
						return min(res, steps)
					} else {
						return steps
					}
				}

				for _, dir := range dirs {
					dr, dc := dir[0], dir[1]
					row, col := r+dr, c+dc

					rowInBounds := row >= 0 && row < ROWS
					colInBounds := col >= 0 && col < COLS
					if rowInBounds && colInBounds && !visited[[2]int{row, col}] {
						visited[[2]int{row, col}] = true
						if grid[row][col] == 0 {
							queue = append(queue, [2]int{row, col})
						} else {
							if k > 0 {
								copyVisited := map[[2]int]bool{}
								id := [2]int{}
								for id, copyVisited[id] = range visited {
								}
								if val := bfs(row, col, k-1, steps+1, copyVisited); val != -1 {
									res = min(res, val)
								}
							}
						}
					}
				}
			}
			steps += 1
		}

		if res != math.MaxInt {
			return res
		}

		return -1
	}

	return bfs(0, 0, k, 0, map[[2]int]bool{})
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
