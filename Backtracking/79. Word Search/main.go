// https://leetcode.com/problems/word-search/
package main

import "fmt"

// 20221006
// Runtime: 873 ms
// Memory Usage: 2.3 MB
// search pruning, don't enter dfs search if state is invalid
// T:O(m*n * 4^L), 4 directions, L is len(word)
func existOptimized(board [][]byte, word string) bool {
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	visited := map[[2]int]bool{}
	ROWS, COLS := len(board), len(board[0])

	var dfs func(state string, r, c int) bool
	dfs = func(state string, r, c int) bool {
		if state == "" {
			return true
		}

		if board[r][c] != state[0] {
			return false
		}

		if visited[[2]int{r, c}] {
			return false
		}

		visited[[2]int{r, c}] = true
		old := state

		if board[r][c] == state[0] {
			state = state[1:]

			// edge case: [["A"]], "A"
			if state == "" {
				return true
			}

			for _, dir := range dirs {
				dr, dc := dir[0], dir[1]
				row, col := r+dr, c+dc

				rowInBound := row >= 0 && row < ROWS
				colInBound := col >= 0 && col < COLS
				if rowInBound && colInBound {
					if dfs(state, row, col) {
						return true
					}
				}
			}
		}

		state = old
		visited[[2]int{r, c}] = false // backtracking

		return false
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if board[r][c] != word[0] {
				continue
			}

			if dfs(word, r, c) {
				return true
			}
		}
	}

	return false
}

// Success
// Details
// Runtime: 2437 ms, faster than 5.09% of Go online submissions for Word Search.
// Memory Usage: 7.7 MB, less than 8.13% of Go online submissions for Word Search.
// T:O(m*n*4dfs) = O(m*n*4^dfs-height), dfs-height will be L which L is len(word) because dfs will run through every characters in word
//
//	= O(mn*4^L)
func exist(board [][]byte, word string) bool {
	visited := map[string]bool{}

	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[0]); col++ {
			if explore(board, word, row, col, visited) {
				return true
			}
		}
	}

	return false
}

func explore(board [][]byte, word string, row, col int, visited map[string]bool) bool {
	if len(word) == 0 {
		return true
	}

	rowInBounds := row >= 0 && row < len(board)
	colInBounds := col >= 0 && col < len(board[0])
	if !rowInBounds || !colInBounds {
		return false
	}

	letter := word[0]
	word = word[1:]
	if board[row][col] != letter {
		return false
	}

	key := fmt.Sprintf("%d,%d", row, col)
	if visited[key] {
		return false
	}

	visited[key] = true

	didExist := explore(board, word, row-1, col, visited)
	visited[key] = false
	if didExist {
		return true
	}

	visited[key] = true
	didExist = explore(board, word, row+1, col, visited)
	if didExist {
		return true
	}
	visited[key] = false

	visited[key] = true
	didExist = explore(board, word, row, col-1, visited)
	if didExist {
		return true
	}
	visited[key] = false

	visited[key] = true
	didExist = explore(board, word, row, col+1, visited)
	visited[key] = false

	return didExist
}

func exploreCompact(board [][]byte, word string, row, col int, visited map[string]bool) bool {
	if len(word) == 0 {
		return true
	}

	rowInBounds := row >= 0 && row < len(board)
	colInBounds := col >= 0 && col < len(board[0])
	if !rowInBounds || !colInBounds {
		return false
	}

	letter := word[0]
	word = word[1:]
	if board[row][col] != letter {
		return false
	}

	key := fmt.Sprintf("%d,%d", row, col)
	if visited[key] {
		return false
	}

	visited[key] = true

	didExist := explore(board, word, row-1, col, visited) ||
		explore(board, word, row+1, col, visited) ||
		explore(board, word, row, col-1, visited) ||
		explore(board, word, row, col+1, visited)

	visited[key] = false

	return didExist
}
