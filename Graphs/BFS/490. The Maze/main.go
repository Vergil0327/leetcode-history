// https://www.cnblogs.com/grandyang/p/6381458.html

package main

/*
Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)
*/

func maze(maze [][]int, start, destination [2]int) bool {
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	var dfs func(startRow, startCol, endRow, endCol int) bool
	dfs = func(startRow, startCol, endRow, endCol int) bool {
		if startRow == endRow && startCol == endCol {
			return true
		}

		if maze[startRow][startCol] == -1 {
			return false
		}

		maze[startRow][startCol] = -1 // mark as visited

		res := false
		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]
			row, col := startRow+dr, startCol+dc
			for row >= 0 && row < len(maze) && col >= 0 && col < len(maze[0]) && maze[row][col] != 1 {
				row, col = row+dr, col+dc
			}
			// hit boundary after for-loop
			row, col = row-dr, col-dc // one step back & check if this is our target
			res = res || dfs(row, col, endRow, endCol)
		}

		return res
	}

	return dfs(start[0], start[1], destination[0], destination[1])
}
