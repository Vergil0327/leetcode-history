// https://leetcode.com/problems/rotate-image/
package main

/*
Input: matrix = [[1,2,3],
								 [4,5,6],
								 [7,8,9]]
Output: [[7,4,1],
				 [8,5,2],
				 [9,6,3]]

Input: matrix = [[5,1,9,11],
								 [2,4,8,10],
								 [13,3,6,7],
								 [15,14,12,16]]
Output: [[15,13,2,5],
				 [14,3,4,1],
				 [12,6,8,9],
				 [16,7,10,11]]

clockwise or counterclockwise
[[3,2,1], [[7,2,1], [[7,2,1],
 [4,5,6],  [4,5,6],  [4,5,6],
 [7,8,9]]  [3,8,9]]  [9,8,3]]

[[3,4,1], [[3,4,1], [[3,4,1],
 [2,5,6],  [8,5,6],  [8,5,2],
 [7,8,9]]  [7,2,9]]  [7,6,9]]

沿著y=-x+1翻轉(左上右下對角線)(transpose?), y=x翻轉(右上左下對角線)也可以
然後再左右翻轉
[[1,2,3], [[1,4,7],
 [4,5,6],  [2,5,8],
 [7,8,9]]  [3,6,9]]

ROWS = COLS = N
*/

// in-place
func rotate(matrix [][]int) {
	N := len(matrix)

	for i := 0; i < N; i++ {
		for j := i; j < N; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N/2; j++ {
			matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
		}
	}
}

// explanation: https://www.youtube.com/watch?v=fMSJSS7eO1w
func rotateSquareRotate(matrix [][]int) {
	l, r := 0, len(matrix)-1
	for l < r {
		for i := 0; i < r-l; i++ {
			top, bottom := l, r

			// save top-left to temp
			topLeft := matrix[top][l+i]

			// bottom-left to top-left
			matrix[top][l+i] = matrix[bottom-i][l]

			// bottom-right to bottom-left
			matrix[bottom-i][l] = matrix[bottom][r-i]

			// top-right to bottm-left
			matrix[bottom][r-i] = matrix[top+i][r]

			// tmp to top-right
			matrix[top+i][r] = topLeft
		}
		l, r = l+1, r-1
	}
}
