// https://leetcode.com/problems/search-a-2d-matrix-ii/
package main

// search from matrix[0][0] to matrix[m-1][n-1]
// based on matrix's properties:
//   - Integers in each row are sorted in ascending from left to right.
//   - Integers in each column are sorted in ascending from top to bottom.
//
// we can search from bottom-left to top-right:
//   - if value > target, move up
//   - if value < target, move right
//   - if not found, we'll out of bound
//
// T:O(m+n)
func searchMatrix(matrix [][]int, target int) bool {
	ROW, COL := len(matrix), len(matrix[0])

	r, c := ROW-1, 0
	for r >= 0 && c < COL {
		if matrix[r][c] > target {
			r -= 1
		} else if matrix[r][c] < target {
			c += 1
		} else {
			return true
		}
	}
	return false
}
