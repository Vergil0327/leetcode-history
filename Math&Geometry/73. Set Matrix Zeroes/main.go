// https://leetcode.com/problems/set-matrix-zeroes/
package main

import "math"

/*
Input: matrix = [[1,1,1],
								 [1,0,1],
								 [1,1,1]]
Output: [[1,0,1],
				 [0,0,0],
				 [1,0,1]]

Input: matrix = [[0,1,2,0],
								 [3,4,5,2],
								 [1,3,1,5]]
Output: [[0,0,0,0],
				 [0,4,5,0],
				 [0,3,1,0]]
*/

// explanation: https://www.youtube.com/watch?v=T41rL0L3Pnw
// T:O(m*n) M:O(1)
func setZeroes(matrix [][]int) {
	ROW, COL := len(matrix), len(matrix[0])

	// memorize zero in first row & column
	// and use extra variable for first row because [0,0] is used for first column
	rowZero := false
	for r := 0; r < ROW; r++ {
		for c := 0; c < COL; c++ {
			if matrix[r][c] == 0 {
				matrix[0][c] = 0
				if r > 0 {
					matrix[r][0] = 0
				} else {
					rowZero = true
				}
			}
		}
	}

	for r := 1; r < ROW; r++ {
		for c := 1; c < COL; c++ {
			if matrix[0][c] == 0 || matrix[r][0] == 0 {
				matrix[r][c] = 0
			}
		}
	}

	// check first column
	if matrix[0][0] == 0 {
		for r := 0; r < ROW; r++ {
			matrix[r][0] = 0
		}
	}

	// check first row
	if rowZero {
		for c := 0; c < COL; c++ {
			matrix[0][c] = 0
		}
	}
}

// brute force, use placeholder (must out of range)
// T:O(n^4) M:O(1)
func setZeroesBruteForce(matrix [][]int) {
	ROW, COL := len(matrix), len(matrix[0])

	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			if matrix[i][j] == 0 {
				for r := 0; r < ROW; r++ {
					for c := 0; c < COL; c++ {
						if matrix[r][c] != 0 && (r == i || c == j) {
							matrix[r][c] = math.MaxInt
						}
					}
				}
			}
		}
	}
	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			if matrix[i][j] == math.MaxInt {
				matrix[i][j] = 0
			}
		}
	}
}

// T:O(n^3) M:O(1)
func setZeroesBruteForceBetter(matrix [][]int) {
	ROW, COL := len(matrix), len(matrix[0])

	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			if matrix[i][j] == 0 {
				for r := 0; r < ROW; r++ {
					if matrix[r][j] != 0 {
						matrix[r][j] = math.MaxInt
					}
				}
				for c := 0; c < COL; c++ {
					if matrix[i][c] != 0 {
						matrix[i][c] = math.MaxInt
					}
				}
			}
		}
	}
	for i := 0; i < ROW; i++ {
		for j := 0; j < COL; j++ {
			if matrix[i][j] == math.MaxInt {
				matrix[i][j] = 0
			}
		}
	}
}
