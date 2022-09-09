// https://leetcode.com/problems/spiral-matrix-ii/
package main

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}

	top, bottom := 0, n
	left, right := 0, n

	num := 1
	for top < bottom && left < right {
		for i := left; i < right; i++ {
			matrix[top][i] = num
			num += 1
		}
		top += 1

		for i := top; i < bottom; i++ {
			matrix[i][right-1] = num
			num += 1
		}
		right -= 1

		for i := right - 1; i >= left; i-- {
			matrix[bottom-1][i] = num
			num += 1
		}
		bottom -= 1

		for i := bottom - 1; i >= top; i-- {
			matrix[i][left] = num
			num += 1
		}
		left += 1
	}

	return matrix
}
