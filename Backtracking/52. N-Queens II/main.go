// https://leetcode.com/problems/n-queens-ii/

package main

const P string = "."
const Q string = "Q"

func totalNQueens(n int) int {
	board := make([][]string, n)
	for i := range board {
		board[i] = make([]string, n)
		for j := range board[0] {
			board[i][j] = P
		}
	}

	res := 0

	//  posDiag: row + col == const. (0,3),(1,2),(2,1)
	//  negDiag: row - col == const. (0,0),(1,1),(2,2)
	colMap, posDiag, negDiag := map[int]bool{}, map[int]bool{}, map[int]bool{}

	var dfs func(row int)
	dfs = func(row int) {
		if row == n {
			res += 1
			return
		}

		for c := 0; c < n; c++ {
			if existed, ok := colMap[c]; existed && ok {
				continue
			}
			if existed, ok := posDiag[row+c]; existed && ok {
				continue
			}
			if existed, ok := negDiag[row-c]; existed && ok {
				continue
			}

			colMap[c] = true
			posDiag[row+c] = true
			negDiag[row-c] = true
			board[row][c] = Q

			dfs(row + 1)

			colMap[c] = false
			posDiag[row+c] = false
			negDiag[row-c] = false
			board[row][c] = P
		}
	}

	dfs(0)

	return res
}
