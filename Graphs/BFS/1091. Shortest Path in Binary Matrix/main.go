package main

// Runtime: 101 ms, faster than 51.57% of Go online submissions for Shortest Path in Binary Matrix.
// Memory Usage: 7.9 MB, less than 61.01% of Go online submissions for Shortest Path in Binary Matrix.
// T:O(m*n), M:O(m*n)
func shortestPathBinaryMatrix(grid [][]int) int {
	// !!! EDGE CASE: bottom-right can't be 1
	if grid[len(grid)-1][len(grid[0])-1] == 1 {
		return -1
	}

	queue := [][2]int{[2]int{0, 0}} // [row,col]
	visited := map[[2]int]bool{}
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}

	length := 1
	for len(queue) > 0 {
		for _, node := range queue {
			queue = queue[1:]

			if node == [2]int{len(grid) - 1, len(grid[0]) - 1} {
				return length
			}

			// !!! EDGE CASE: path can't contains 1
			if grid[node[0]][node[1]] == 1 {
				continue
			}

			for _, dir := range dirs {
				dr, dc := dir[0], dir[1]
				row, col := node[0]+dr, node[1]+dc
				rowInBounds := row >= 0 && row < len(grid)
				colInBounds := col >= 0 && col < len(grid[0])
				if nxt := [2]int{row, col}; rowInBounds && colInBounds && !visited[nxt] {
					visited[nxt] = true
					queue = append(queue, nxt)
				}
			}
		}

		length += 1
	}

	return -1
}
