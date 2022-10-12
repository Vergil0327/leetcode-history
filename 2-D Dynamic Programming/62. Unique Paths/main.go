// https://leetcode.com/problems/unique-paths/
package main

import "fmt"

/*
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
*/

// https://www.youtube.com/watch?v=IlEsdxuD4lY
// or https://leetcode.com/problems/unique-paths/discuss/22954/C%2B%2B-DP
// T:O(m*n) M:O(m*n)
func uniquePathsDP(m int, n int) int {
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
		dp[i][0] = 1 // only 1 way to go down in first column
		if i == 0 {
			for j := 0; j < n; j++ {
				dp[i][j] = 1 // only 1 way to go right in first row
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			// comes from either left or top position
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		}
	}

	return dp[m-1][n-1]
}

// since we only update current row
func uniquePathsDP_Optimized(m int, n int) int {
	dp := make([]int, n)
	prevRow := make([]int, n)
	for i := 0; i < n; i++ {
		prevRow[i] = 1
	}
	dp[0] = 1 // only 1 way to go right in first column

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			// we can reduce dp[i][j] = dp[i-1][j] + dp[i][j-1] to:
			dp[j] = prevRow[j] + dp[j-1]
		}
		dp, prevRow = prevRow, dp
	}

	// return dp[n-1] // !!! be careful! we'll swap after nested for-loop
	return prevRow[n-1]
}

// solution: https://leetcode.com/problems/unique-paths/discuss/182143/Recursive-memoization-and-dynamic-programming-solutions
func uniquePaths(m int, n int) int {
	memo := map[string]int{}

	var dfs func(row, col int, memo map[string]int) int
	dfs = func(row, col int, memo map[string]int) int {
		if row == m-1 && col == n-1 {
			return 1
		}

		rowInBounds := row >= 0 && row < m
		colInBounds := col >= 0 && col < n
		if !rowInBounds || !colInBounds {
			return 0
		}

		if paths, ok := memo[fmt.Sprintf("%d,%d", row, col)]; ok {
			return paths
		}

		uniqPathsAtCurrPos := dfs(row+1, col, memo) + dfs(row, col+1, memo)
		memo[fmt.Sprintf("%d,%d", row, col)] = uniqPathsAtCurrPos
		return uniqPathsAtCurrPos
	}

	return dfs(0, 0, memo)
}

func uniquePathsBruteForce(m int, n int) int {
	var dfs func(row, col int) int
	dfs = func(row, col int) int {
		if row == m-1 && col == n-1 {
			return 1
		}

		rowInBounds := row >= 0 && row < m
		colInBounds := col >= 0 && col < n
		if !rowInBounds || !colInBounds {
			return 0
		}

		return dfs(row+1, col) + dfs(row, col+1)
	}

	return dfs(0, 0)
}

// Math solution
// Total permutations = (m+n)! / (m! * n!)
// explanation: https://leetcode.com/problems/unique-paths/discuss/22958/Math-solution-O(1)-space
func uniquePathsMath(m int, n int) int {
	if m == 1 || n == 1 {
		return 1
	}

	m--
	n--
	if m < n {
		m, n = n, m
	}

	result := 1
	j := 1
	for i := m + 1; i <= m+n; i, j = i+1, j+1 {
		result *= i
		result /= j
	}

	return result
}
