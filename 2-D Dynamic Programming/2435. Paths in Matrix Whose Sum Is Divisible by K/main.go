package main

const mod = int(1e9 + 7)

// T:O((m*n)^2)
func numberOfPaths(grid [][]int, k int) int {
	ROWS, COLS := len(grid), len(grid[0])

	// we can't use:
	// > memo := map[string]int{} or map[[3]int]int{}
	// > key := fmt.Sprintf("%d,%d,%d", row, col, sum) or [3]int{row, col, sum}
	// we'll get TLE when use hashmap.
	// access efficiency of slice is way more faster than hashmap
	memo := make([][][]int, ROWS)
	for i := range memo {
		memo[i] = make([][]int, COLS)
		for j := range memo[i] {
			memo[i][j] = make([]int, k)
			for m := range memo[i][j] {
				memo[i][j][m] = -1
			}
		}
	}

	var dfs func(remainder, row, col int) int
	dfs = func(remainder, row, col int) int {
		rowInBounds, colInBounds := row >= 0 && row < ROWS, col >= 0 && col < COLS
		if !(rowInBounds && colInBounds) {
			return 0
		}

		remainder = (remainder + grid[row][col]) % k
		if row == ROWS-1 && col == COLS-1 {
			if remainder%k == 0 {
				memo[row][col][remainder] = 1
				return 1
			}

			memo[row][col][remainder] = 0
			return 0
		}

		if v := memo[row][col][remainder]; v != -1 {
			return memo[row][col][remainder]
		}

		memo[row][col][remainder] = (dfs(remainder, row+1, col) + dfs(remainder, row, col+1)) % mod
		return memo[row][col][remainder]
	}

	return dfs(0, 0, 0)
}
