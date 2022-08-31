// https://leetcode.com/problems/rotting-oranges/
package main

import "fmt"

/*
Example 1:
Input: grid = [[2,1,1],
							 [1,1,0],
							 [0,1,1]]
Output: 4


Example 2:
Input: grid = [[2,1,1],
							 [0,1,1],
							 [1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

[[2,1,1],
 [1,1,1],
 [0,1,2]]
*/

const E int = 0 // emtpy
const F int = 1 // fresh
const R int = 2 // rotten

// explanation: https://www.youtube.com/watch?v=y704fEOx0s0
func orangesRottingBetter(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])

	// keep tracking of elapse time & fresh orange
	time, fresh := 0, 0
	queue := [][]int{} // [[row, col], ...] for BFS
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if grid[r][c] == F {
				fresh += 1
			}

			if grid[r][c] == R {
				queue = append(queue, []int{r, c})
			}
		}
	}
	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 && fresh > 0 {
		for _, entry := range queue {
			r, c := entry[0], entry[1]
			queue = queue[1:]

			for _, direction := range directions {
				dr, dc := direction[0], direction[1]
				row, col := r+dr, c+dc

				// if in bounds & it's fresh orange, MAKE IT ROTTEN!
				rowsInBounds := row >= 0 && row < ROWS
				colInBounds := col >= 0 && col < COLS
				if !rowsInBounds || !colInBounds {
					continue
				}

				if grid[row][col] != F {
					continue
				}

				grid[row][col] = R
				fresh -= 1
				queue = append(queue, []int{row, col})
			}
		}

		time += 1
	}

	if fresh > 0 {
		return -1
	} else {
		return time
	}
}

// BFS, each iteration plus 1 minute
// maximun required time will be answer
// ! 注意：因為每次的BFS iteration爛橘子會同時感染四周, 所以要先找出所有爛橘子
// ! 在進行BFS
// ! 另外只有當該次iteration有污染新鮮橘子的時候才增加elapse time
// ! 不然會多算上第一次及最後一次iteration, 其中第一次是起點而最後一次是週遭已沒有新鮮橘子
func orangesRotting(grid [][]int) int {
	visited := map[string]bool{}
	ROWS, COLS := len(grid), len(grid[0])

	queue := [][]int{} // [[r,c], ...]
	var bfs = func() int {
		elapse := 0

		for len(queue) > 0 {
			hasFresh := false
			for _, item := range queue {
				row, col := item[0], item[1]
				queue = queue[1:]

				rowInBounds := row >= 0 && row < ROWS
				colInBounds := col >= 0 && col < COLS
				if !rowInBounds || !colInBounds {
					continue
				}

				if grid[row][col] == E {
					continue
				}

				key := fmt.Sprintf("%d,%d", row, col)
				if visited[key] {
					continue
				}

				visited[key] = true

				if grid[row][col] == F {
					hasFresh = true
					grid[row][col] = R
				}

				queue = append(queue, []int{row + 1, col}, []int{row - 1, col}, []int{row, col + 1}, []int{row, col - 1})
			}

			if hasFresh {
				elapse += 1
			}
		}

		return elapse
	}

	// find all rotten orange position and put all in the queue
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if grid[r][c] == R {
				queue = append(queue, []int{r, c})
			}
		}
	}

	elpaseTime := 0

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			key := fmt.Sprintf("%d,%d", r, c)
			if visited[key] {
				continue
			}

			if grid[r][c] == R {
				// BFS
				time := bfs()
				if time > elpaseTime {
					elpaseTime = time
				}
			}
		}
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if grid[r][c] == F {
				return -1
			}
		}
	}

	return elpaseTime
}
