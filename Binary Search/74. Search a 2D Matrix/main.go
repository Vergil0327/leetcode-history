// https://leetcode.com/problems/search-a-2d-matrix/
package main

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true
// T:O(logM + logN)
func searchMatrix(matrix [][]int, target int) bool {
	// !!! edge case: be cautious of out-of-index error
	if len(matrix) == 0 {
		return false
	}

	if len(matrix) < 2 {
		col := matrix[0]
		// !!! edge case: be cautious of out-of-index error
		if len(col) == 0 {
			return false
		}

		mid := len(col) / 2

		if col[mid] == target {
			return true
		}

		if col[mid] > target {
			col = col[:mid]
			return searchMatrix([][]int{col}, target)
		}

		if col[mid] < target {
			col = col[mid+1:]
			return searchMatrix([][]int{col}, target)
		}
	}

	midRow := len(matrix) / 2
	min, max := matrix[midRow][0], matrix[midRow][len(matrix[midRow])-1]
	if target > max {
		return searchMatrix(matrix[midRow+1:], target)
	}

	if target < min {
		return searchMatrix(matrix[:midRow], target)
	}

	return searchMatrix([][]int{matrix[midRow]}, target)
}

// https://www.youtube.com/watch?v=Ber2pi2C0j0
func searchMatrixWhileLoop(matrix [][]int, target int) bool {
	ROWS, COLS := len(matrix), len(matrix[0])

	top, bot := 0, ROWS-1
	for top <= bot {
		row := (top + bot) / 2
		if target < matrix[row][0] {
			bot = row - 1
		} else if target > matrix[row][len(matrix[row])-1] {
			top = row + 1
		} else {
			break
		}
	}

	if top > bot {
		return false
	}

	row := (top + bot) / 2
	l, r := 0, COLS-1
	for l <= r {
		mid := (l + r) / 2
		if target < matrix[row][mid] {
			r = mid - 1
		} else if target > matrix[row][mid] {
			l = mid + 1
		} else {
			return true
		}
	}
	return false
}
