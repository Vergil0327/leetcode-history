// https://leetcode.com/problems/n-queens/
package main

import (
	"strings"
)

const P string = "."
const Q string = "Q"

// explanation: https://www.youtube.com/watch?v=Ph95IHmRp5M
func solveNQueens(n int) [][]string {
	board := make([][]string, n)
	for i := range board {
		board[i] = make([]string, n)
		for j := 0; j < n; j++ {
			board[i][j] = P
		}
	}

	res := [][]string{}
	colMap := map[int]bool{}
	positiveDiag := map[int]bool{}
	negativeDiag := map[int]bool{}

	var dfs func(row int)
	dfs = func(row int) {
		if row == n {
			cpt := copyBoard(n, board)

			ans := []string{}
			for i := range cpt {
				ans = append(ans, strings.Join(cpt[i], ""))
			}
			res = append(res, ans)
			return
		}

		for c := 0; c < n; c++ {
			if existed, ok := colMap[c]; existed && ok {
				continue
			}
			if existed, ok := positiveDiag[row+c]; existed && ok {
				continue
			}
			if existed, ok := negativeDiag[row-c]; existed && ok {
				continue
			}

			// tracking state
			board[row][c] = Q
			colMap[c] = true
			positiveDiag[row+c] = true
			negativeDiag[row-c] = true

			dfs(row + 1)

			// backtracking, restore state
			board[row][c] = P
			colMap[c] = false
			positiveDiag[row+c] = false
			negativeDiag[row-c] = false
		}
	}

	dfs(0)

	return res
}

func copyBoard(n int, board [][]string) [][]string {
	cpt := make([][]string, n)
	for i := 0; i < n; i++ {
		cpt[i] = make([]string, n)
	}
	copy(cpt, board)
	return cpt
}

// only pass n = 1 to 6
func solveNQueensTimeout(n int) [][]string {
	N := n

	res := [][]string{}

	arrangementQ := map[string]bool{} // remove duplicate

	var putQueen func(state [][]string, n, i, j int)
	putQueen = func(state [][]string, n, i, j int) {
		if n == 0 {
			key := ""
			ans := make([]string, N)
			for i := range ans {
				row := strings.Join(state[i], "")
				key += row
				ans[i] = row
			}

			if existed, ok := arrangementQ[key]; existed && ok {
				return
			}
			arrangementQ[key] = true

			res = append(res, ans)
			return
		}

		nextState := make([][]string, N)
		for i := range nextState {
			nextState[i] = make([]string, N)
		}
		copy(nextState, state)

		if !check(nextState, i, j, N) {
			return
		}

		nextState[i][j] = Q
		n -= 1

		for r := 0; r < N; r++ {
			for c := 0; c < N; c++ {
				putQueen(nextState, n, r, c)
			}
		}

		nextState[i][j] = P // !!! backtracking
	}

	for r := 0; r < N; r++ {
		for c := 0; c < N; c++ {
			board := make([][]string, N)
			for i := range board {
				board[i] = make([]string, N)
			}
			putQueen(board, n, r, c)
		}
	}

	return res
}

func check(state [][]string, row, col, N int) bool {
	for c := 0; c < N; c++ {
		if state[row][c] == Q {
			return false
		}
		state[row][c] = P
	}
	for r := 0; r < N; r++ {
		if state[r][col] == Q {
			return false
		}
		state[r][col] = P
	}
	for r, c := 1, 1; r < N && c < N; r, c = r+1, c+1 {
		if row+r < N && col+c < N {
			if state[row+r][col+c] == Q {
				return false
			}
			state[row+r][col+c] = P
		}
		if row+r < N && col-c >= 0 {
			if state[row+r][col-c] == Q {
				return false
			}
			state[row+r][col-c] = P
		}
		if row-r >= 0 && col+c < N {
			if state[row-r][col+c] == Q {
				return false
			}
			state[row-r][col+c] = P
		}
		if row-r >= 0 && col-c >= 0 {
			if state[row-r][col-c] == Q {
				return false
			}
			state[row-r][col-c] = P
		}
	}
	return true
}
