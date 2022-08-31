package main

const T byte = byte('T')

// REVERSE THINKING
// explanation: https://www.youtube.com/watch?v=9z2BunfoZ5Y
func solveCleverWay(board [][]byte) {
	ROWS, COLS := len(board), len(board[0])

	// 1. (DFS) Capture all unsurrounding regions, turn O to T, T stands for tmp
	// we only need to start checking through all the 'O' on four borders of board
	var dfs func(r, c int)
	dfs = func(r, c int) {
		rowInBounds := r >= 0 && r < ROWS
		colInBounds := c >= 0 && c < COLS
		if !rowInBounds || !colInBounds {
			return
		}

		// ! we can't check like this: board[r][c] == X,
		// ! because we'll turn O to T
		if board[r][c] != O {
			return
		}

		board[r][c] = T
		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c+1)
		dfs(r, c-1)
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if board[r][c] == O && (r == 0 || r == ROWS-1 || c == 0 || c == COLS-1) {
				dfs(r, c)
			}
		}
	}

	// 2. Capture surrounding regions, turn O to X
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if board[r][c] == O {
				board[r][c] = X
			}
		}
	}

	// 3. Uncapture unsurrounding regions, turn T back to O
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if board[r][c] == T {
				board[r][c] = O
			}
		}
	}
}
