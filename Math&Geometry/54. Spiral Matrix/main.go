// https://leetcode.com/problems/spiral-matrix/
package main

/*
Input: matrix = [[1,2,3],
								 [4,5,6],
								 [7,8,9]]
1	2	3	6	9	8	7	4	5
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],
								 [5,6,7,8],
								 [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
*/

/*
	[[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]]

[1,2,3,4,8,12,16,15,14,13,9,5,6,7,10,14]
[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
*/

func spiralOrder(matrix [][]int) []int {
	ROW, COL := len(matrix), len(matrix[0])
	res := []int{}

	L, R := 0, COL-1 // left, right
	T, B := 0, ROW-1 // top, bottom
	i, j := 0, 0

LOOP:
	for len(res) < ROW*COL {
		// top-left > top-right
		for j <= R {
			if len(res) >= ROW*COL {
				break LOOP
			}
			res = append(res, matrix[i][j])
			j += 1
		}

		// reset j & shift i to avoid duplicate
		j = R
		i += 1

		// top-right > bottom-right
		for i <= B {
			if len(res) >= ROW*COL {
				break LOOP
			}

			res = append(res, matrix[i][j])
			i += 1
		}

		// reset i & shift j to avoid duplicate
		i = B
		j -= 1

		// bottom-right > bottom-left
		for j >= L {
			if len(res) >= ROW*COL {
				break LOOP
			}
			res = append(res, matrix[i][j])
			j -= 1
		}
		j = L

		// bottom-left > top-left
		T += 1
		for i > T {
			if len(res) >= ROW*COL {
				break LOOP
			}
			if i-1 >= 0 {
				res = append(res, matrix[i-1][j])
			}
			i -= 1
		}

		L += 1
		R -= 1
		B -= 1

		j = L
	}

	return res
}

// explanation: https://www.youtube.com/watch?v=BJnMZNwUk1M
// T:O(n), T:O(1)
func spiralOrderBetter(matrix [][]int) []int {
	res := []int{}
	left, right := 0, len(matrix[0])
	top, bottom := 0, len(matrix)

	for left < right && top < bottom {
		// get every i in top row
		for i := left; i < right; i++ {
			res = append(res, matrix[top][i])
		}
		top += 1 // move top boundary after we finish top row

		// get every i in the right col
		for i := top; i < bottom; i++ {
			res = append(res, matrix[i][right-1])
		}
		right -= 1 // move right boundary after we finish right col

		// !!! think [[1, 2, 3]] or [[1],[2],[3]] single row or column
		// we need to check our boundary
		if !(left < right && top < bottom) {
			break
		}

		// get every i in bottom row in reverse order
		for i := right - 1; i >= left; i-- {
			res = append(res, matrix[bottom-1][i])
		}
		bottom -= 1 // move bottom boundary after we finish bottom row

		// get every i in left col in verse order
		for i := bottom - 1; i >= top; i-- {
			res = append(res, matrix[i][left])
		}
		left += 1 // move left boundary after we finish left col
	}

	return res
}
