// https://leetcode.com/problems/maximum-rows-covered-by-columns/
package main

import "math"

// T:O(2^n * n^2)
func maximumRows(mat [][]int, cols int) int {
	max := 0
	choose := map[int]struct{}{}

	var dfs func(col, n int)
	dfs = func(col, n int) {
		if n == 0 {
			count := 0
			for r := 0; r < len(mat); r++ {
				coverd := true
				for c := 0; c < len(mat[0]); c++ {
					if _, ok := choose[c]; ok || mat[r][c] == 0 {
						continue
					}
					coverd = false
				}
				if coverd {
					count += 1
				}
			}
			max = int(math.Max(float64(max), float64(count)))
			return
		}

		if col == len(mat[0]) {
			return
		}

		dfs(col+1, n)
		choose[col] = struct{}{}
		dfs(col+1, n-1)
		delete(choose, col)
	}

	dfs(0, cols)
	return max
}
