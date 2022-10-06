package main

// explanation: https://www.youtube.com/watch?v=q63a2oDwmwM
// we can get better efficiency by using array rather than hashmap of hashmap
func solveSudoku(board [][]byte) {
	ROWS, COLS := 9, 9

	row := map[int]map[int]bool{}
	col := map[int]map[int]bool{}
	box := map[[2]int]map[int]bool{} // [row/3, col/3]: 1-9

	// initialization
	for r := 0; r < ROWS; r++ {
		row[r] = make(map[int]bool)
	}
	for c := 0; c < COLS; c++ {
		col[c] = make(map[int]bool)
	}
	for r := 0; r < ROWS/3; r++ {
		for c := 0; c < COLS/3; c++ {
			box[[2]int{r, c}] = make(map[int]bool)
		}
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if board[r][c] != '.' {
				v := int(board[r][c] - '0')

				row[r][v] = true
				col[c][v] = true
				box[[2]int{r / 3, c / 3}][v] = true
			}
		}
	}

	var dfs func(board [][]byte, r, c int) bool
	dfs = func(board [][]byte, r, c int) bool {
		if r == 9 {
			return true
		}
		if c == 9 {
			return dfs(board, r+1, 0)
		}

		// already has value -> skip
		if board[r][c] != '.' {
			return dfs(board, r, c+1)
		} else {

			// try them all (1-9)
			for v := 1; v <= 9; v++ {
				if row[r][v] || col[c][v] || box[[2]int{r / 3, c / 3}][v] {
					continue
				}

				board[r][c] = byte(v + '0')
				row[r][v], col[c][v] = true, true
				box[[2]int{r / 3, c / 3}][v] = true

				// if true, means we've finished sudoku. directly return true to exit the loop
				if dfs(board, r, c+1) {
					return true
				}

				// restore for backtracking
				board[r][c] = '.'
				row[r][v], col[c][v] = false, false
				box[[2]int{r / 3, c / 3}][v] = false
			}
			return false
		}
	}

	dfs(board, 0, 0)
	return
}

func solveSudokuSample3MSSolution(board [][]byte) {
	cols := make([][]bool, 9)
	for i := 0; i < 9; i++ {
		cols[i] = make([]bool, 10)
	}

	rows := make([][]bool, 9)
	for i := 0; i < 9; i++ {
		rows[i] = make([]bool, 10)
	}

	boxes := make([][][]bool, 3)
	for i := 0; i < 3; i++ {
		boxes[i] = make([][]bool, 3)
		for j := 0; j < 3; j++ {
			boxes[i][j] = make([]bool, 10)
		}
	}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				continue
			}

			ch := int(board[i][j] - '0')
			rows[i][ch], cols[j][ch], boxes[i/3][j/3][ch] = true, true, true
		}
	}

	var fill func(board [][]byte, i, j int, rows, cols [][]bool, boxes [][][]bool) bool
	fill = func(board [][]byte, i, j int, rows, cols [][]bool, boxes [][][]bool) bool {
		if i == 9 {
			return true
		}

		if j == 9 {
			return fill(board, i+1, 0, rows, cols, boxes)
		}

		if board[i][j] != '.' {
			return fill(board, i, j+1, rows, cols, boxes)
		}

		for k := 1; k <= 9; k++ {
			if rows[i][k] || cols[j][k] || boxes[i/3][j/3][k] {
				continue
			}

			rows[i][k], cols[j][k], boxes[i/3][j/3][k] = true, true, true

			board[i][j] = byte(k + '0')
			if fill(board, i, j+1, rows, cols, boxes) {
				return true
			}

			rows[i][k], cols[j][k], boxes[i/3][j/3][k] = false, false, false

			board[i][j] = '.'
		}

		return false
	}

	fill(board, 0, 0, rows, cols, boxes)
}
