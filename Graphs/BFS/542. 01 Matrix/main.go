package main

import "math"

// explanation: https://www.youtube.com/watch?v=hIvMZFqjs_A
// ! we can see that for any 1 position from any "nearest" 0, the sum is the same
// maybe we should start from every zero position as 1st level(or depth) of queue
// the next level(or depth) would be the previous updated 1
// continue updating the matrix...
func updateMatrix(mat [][]int) [][]int {
	ROWS, COLS := len(mat), len(mat[0])
	const placeholder = math.MaxInt

	queue := [][2]int{} // [row, col]
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if mat[r][c] == 0 {
				queue = append(queue, [2]int{r, c}) // first level
			} else {
				mat[r][c] = placeholder // use MaxInt as placeholder to mark position we want to update
			}
		}
	}

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 {
		for _, pos := range queue {
			queue = queue[1:]

			r, c := pos[0], pos[1]
			for _, dir := range dirs {
				dr, dc := dir[0], dir[1]
				row, col := r+dr, c+dc

				rowInBounds := row >= 0 && row < ROWS
				colInBounds := col >= 0 && col < COLS
				if nxt := [2]int{row, col}; rowInBounds && colInBounds && mat[row][col] == placeholder {
					mat[row][col] = mat[r][c] + 1 // trick here, we can start from 0 and increment 1 by 1 to update level by level
					queue = append(queue, nxt)    // next level traversal
				}
			}
		}
	}

	return mat
}

// if we starts from 1, we end up m*n*O(bfs) because we caluculate at each 1 position
// lets try update matrix from zero
// TLE at 41 / 50 test cases passed.
func updateMatrixStilTLC(mat [][]int) [][]int {
	ROWS, COLS := len(mat), len(mat[0])
	res := make([][]int, ROWS)
	for i := range res {
		res[i] = make([]int, COLS)
		for j := range res[0] {
			res[i][j] = math.MaxInt
		}
	}

	var bfs func(i, j int) = func(i, j int) {
		dst := 1
		visited := map[[2]int]bool{}
		dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		queue := [][2]int{{i, j}}
		for len(queue) > 0 {
			for _, pos := range queue {
				queue = queue[1:]
				r, c := pos[0], pos[1]

				for _, dir := range dirs {
					dr, dc := dir[0], dir[1]
					row, col := r+dr, c+dc

					rowInBounds := row >= 0 && row < ROWS
					colInBounds := col >= 0 && col < COLS
					if rowInBounds && colInBounds && mat[row][col] == 1 {
						nxt := [2]int{row, col}
						if !visited[nxt] {
							visited[nxt] = true
							if dst < res[row][col] {
								res[row][col] = dst
							}
							queue = append(queue, nxt)
						}
					}
				}
			}
			dst += 1
		}
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if mat[r][c] == 0 {
				res[r][c] = 0
				bfs(r, c)
			}
		}
	}

	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

// TLE
func updateMatrixBruteForce(mat [][]int) [][]int {
	ROWS, COLS := len(mat), len(mat[0])
	res := make([][]int, ROWS)
	for i := range res {
		res[i] = make([]int, COLS)
	}

	var bfs func(i, j int) int = func(i, j int) int {
		dst := 0
		dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		visited := map[[2]int]bool{}
		queue := [][2]int{[2]int{i, j}}
		for len(queue) > 0 {
			for _, pos := range queue {
				queue = queue[1:]

				r, c := pos[0], pos[1]

				if mat[r][c] == 0 {
					return dst
				}

				for _, dir := range dirs {
					dr, dc := dir[0], dir[1]
					row, col := r+dr, c+dc

					rowInBounds := row >= 0 && row < ROWS
					colInBounds := col >= 0 && col < COLS
					key := [2]int{row, col}
					if rowInBounds && colInBounds && !visited[key] {
						visited[key] = true
						queue = append(queue, key)
					}
				}
			}
			dst += 1
		}

		return dst
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if mat[r][c] == 0 {
				res[r][c] = 0
				continue
			} else {
				res[r][c] = bfs(r, c)
			}
		}
	}

	return res
}
