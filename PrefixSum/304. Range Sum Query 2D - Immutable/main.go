package main

type NumMatrix struct {
	sum [][]int
}

// explanation: https://www.youtube.com/watch?v=KE8MQuwE2yA
// O(n^2)
func ConstructorOptimized(matrix [][]int) NumMatrix {
	ROWS, COLS := len(matrix), len(matrix[0])

	mat := make([][]int, ROWS+1)
	for r := range mat {
		mat[r] = make([]int, COLS+1)
	}

	for r := 0; r < ROWS; r++ {
		prefix := 0
		for c := 0; c < COLS; c++ {
			prefix += matrix[r][c]
			above := mat[r][c+1]
			mat[r+1][c+1] = prefix + above
		}
	}

	return NumMatrix{sum: mat}
}

/*
T: O(1)

X X X
X O O
X O O
3x3 - 1x3 - 3x1 + 1x1
*/
func (this *NumMatrix) SumRegionOptimized(row1 int, col1 int, row2 int, col2 int) int {
	// offset to prefix sum's index
	row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1

	bottomRight := this.sum[row2][col2]
	above := this.sum[row1-1][col2]
	left := this.sum[row2][col1-1]
	topLeft := this.sum[row1-1][col1-1]
	return bottomRight - above - left + topLeft
}

/* 20221012 first try */

// each row is independent prefix sum, O(n^2)
func Constructor(matrix [][]int) NumMatrix {
	ROWS, COLS := len(matrix), len(matrix[0])
	arr := make([][]int, ROWS)
	for r := range arr {
		arr[r] = make([]int, COLS+1)
		for c := 0; c < COLS; c++ {
			arr[r][c+1] = arr[r][c] + matrix[r][c]
		}
	}

	return NumMatrix{sum: arr}
}

// T:O(row)
func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	if row1 == row2 && col1 == col2 {
		total := this.sum[row2][col2+1]
		if col2 >= 0 {
			total -= this.sum[row2][col2]
		}
		return total
	}

	total := 0
	for r := row1; r <= row2; r++ {
		total += this.sum[r][col2+1]
		if col1 >= 0 {
			total -= this.sum[r][col1]
		}
	}

	return total
}
