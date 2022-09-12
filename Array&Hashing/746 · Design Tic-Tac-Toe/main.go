// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/design-tic-tac-toe/
package main

const P1 int = 1
const P2 int = 2

type TicTacToe struct {
	board [][]int

	// for  T:O(1) optimized check
	size    int
	row     []int
	col     []int
	posDiag int // positive diagonal
	negDiag int // negative diagonal
}

// create n x n board
func NewTicTacToe(n int) TicTacToe {
	board := make([][]int, n)
	for i := range board {
		board[i] = make([]int, n)
	}

	return TicTacToe{
		board: board,
		size:  n,
		row:   make([]int, n),
		col:   make([]int, n),
	}
}

/*
player: 1 or 2
return: true if win
*/
func (this *TicTacToe) Move(row, col int, player int) bool {
	this.board[row][col] = player
	// return this.check(row, col, player)
	return this.checkOptimized(row, col, player)
}

func (this *TicTacToe) checkOptimized(row, col, player int) bool {
	N := this.size
	if player == P1 {
		this.row[row] += 1
		this.col[col] += 1
		// (0,0), (1,1), (2,2)
		if row == col {
			this.negDiag += 1
		}
		// (2,0), (1,1), (0,2)
		if row+col == N-1 {
			this.posDiag += 1
		}

		if this.row[row] == N || this.col[col] == N || this.posDiag == N || this.negDiag == N {
			return true
		} else {
			return false
		}

	} else {
		this.row[row] -= 1
		this.col[col] -= 1
		if row == col {
			this.negDiag -= 1
		}
		if row+col == N-1 {
			this.posDiag -= 1
		}

		if this.row[row] == -N || this.col[col] == -N || this.posDiag == -N || this.negDiag == -N {
			return true
		} else {
			return false
		}
	}
}

// can be optimized to T:O(1)
// see: https://www.youtube.com/watch?v=3iONGQqlj_I
// T:O(n)
func (this *TicTacToe) check(row, col, player int) bool {
	N := this.size

	vertical := 0
	for r := 0; r < N; r++ {
		if this.board[r][col] == player {
			vertical += 1
		} else {
			break
		}
	}
	if vertical == N {
		return true
	}

	horizontal := 0
	for c := 0; c < N; c++ {
		if this.board[row][c] == player {
			horizontal += 1
		} else {
			break
		}
	}
	if horizontal == N {
		return true
	}

	if row == col {
		diagNeg := 0
		for r, c := 0, 0; r < N; r, c = r+1, c+1 {
			if this.board[r][c] == player {
				diagNeg += 1
			} else {
				break
			}
		}
		if diagNeg == N {
			return true
		}
	}

	if row+col == N-1 {
		diagPos := 0
		for r, c := 0, N-1; r < N && c >= 0; r, c = r+1, c-1 {
			if this.board[r][c] == player {
				diagPos += 1
			} else {
				break
			}
		}
		if diagPos == N {
			return true
		}
	}

	return false
}
