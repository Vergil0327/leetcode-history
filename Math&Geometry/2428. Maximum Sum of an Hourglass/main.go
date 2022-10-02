package main

// T:O(m*n*7), sum of hourglass would be constant
func maxSum(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])

	maxSum := 0
	for row := 0; row < ROWS-2; row++ {
		for col := 0; col < COLS-2; col++ {
			sum := 0
			for c := col; c <= col+2; c++ {
				sum += grid[row][c]
			}
			sum += grid[row+1][col+1]
			for c := col; c <= col+2; c++ {
				sum += grid[row+2][c]
			}

			if sum > maxSum {
				maxSum = sum
			}
		}
	}

	return maxSum
}
