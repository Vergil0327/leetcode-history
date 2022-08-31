// https://leetcode.com/problems/surrounded-regions/
package main

import "fmt"

/*
Example 1:
Input: board = [["X","X","X","X"],
								["X","O","O","X"],
								["X","X","O","X"],
								["X","O","X","X"]]
Output: [["X","X","X","X"],
				 ["X","X","X","X"],
				 ["X","X","X","X"],
				 ["X","O","X","X"]]

Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
*/

const X byte = byte('X')
const O byte = byte('O')

func solve(board [][]byte) {
	borders := map[string]bool{}
	ROWS, COLS := len(board), len(board[0])
	for r := 0; r < ROWS; r++ {
		key := fmt.Sprintf("%d,%d", r, 0)
		borders[key] = true

		key = fmt.Sprintf("%d,%d", r, COLS-1)
		borders[key] = true
	}
	for c := 0; c < COLS; c++ {
		key := fmt.Sprintf("%d,%d", 0, c)
		borders[key] = true

		key = fmt.Sprintf("%d,%d", ROWS-1, c)
		borders[key] = true
	}

	shouldFlip := [][]int{} // [][row, col]{}
	visited := map[string]bool{}
	for r := 0; r < len(board); r++ {
		for c := 0; c < len(board[0]); c++ {
			cell := board[r][c]
			if cell == X {
				continue
			}

			if explore(board, r, c, visited, &shouldFlip) {
				if !checkIfTouchBoarder(borders, shouldFlip) {
					// flip
					for _, entry := range shouldFlip {
						row, col := entry[0], entry[1]
						board[row][col] = X
					}
				}
				shouldFlip = [][]int{}
			}
		}
	}
}

func explore(board [][]byte, r, c int, visited map[string]bool, shouldFlip *[][]int) bool {
	rowInBounds := r >= 0 && r < len(board)
	colInBounds := c >= 0 && c < len(board[0])
	if !rowInBounds || !colInBounds {
		return false
	}

	if board[r][c] == X {
		return false
	}

	key := fmt.Sprintf("%d,%d", r, c)
	if _, ok := visited[key]; ok {
		return false
	}

	visited[key] = true

	*shouldFlip = append(*shouldFlip, []int{r, c})

	explore(board, r+1, c, visited, shouldFlip)
	explore(board, r-1, c, visited, shouldFlip)
	explore(board, r, c+1, visited, shouldFlip)
	explore(board, r, c-1, visited, shouldFlip)

	return true
}

func checkIfTouchBoarder(borders map[string]bool, cells [][]int) bool {
	for _, entry := range cells {
		r, c := entry[0], entry[1]
		key := fmt.Sprintf("%d,%d", r, c)
		if touched, ok := borders[key]; touched && ok {
			return true
		}
	}

	return false
}
