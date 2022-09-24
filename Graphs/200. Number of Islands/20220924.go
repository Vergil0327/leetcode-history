package main

// T:O(m*n)
func numIslandsUnionFind(grid [][]byte) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	// union-find
	count := 0 // count of island
	ROWS, COLS := len(grid), len(grid[0])
	parent := make([]int, ROWS*COLS)
	rank := make([]int, ROWS*COLS)

	// init
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if grid[r][c] == '1' {
				id := r*COLS + c
				parent[id] = id
				rank[id] = 1
				count += 1
			}
		}
	}

	// id := r*COLS + c
	// T:O(1) approximately with path compression, worst T:O(n)
	var find func(id int) int = func(id int) int {
		p := parent[id]

		// path compression
		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	// T:O(1)
	var union func(id1, id2 int) bool = func(id1, id2 int) bool {
		p1, p2 := find(id1), find(id2)

		// already connected
		if p1 == p2 {
			return false
		}

		if rank[p1] > rank[p2] {
			parent[p2] = p1
			rank[p1] += rank[p2]
		} else {
			parent[p1] = p2
			rank[p2] += rank[p1]
		}

		return true
	}

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if grid[r][c] == '1' {
				for _, dir := range dirs {
					dr, dc := dir[0], dir[1]
					row, col := r+dr, c+dc

					rowInBounds := row >= 0 && row < ROWS
					colInBounds := col >= 0 && col < COLS
					if rowInBounds && colInBounds && grid[row][col] == '1' {
						node1 := r*COLS + c
						node2 := row*COLS + col
						if union(node1, node2) {
							count -= 1
						}
					}
				}
			}
		}
	}

	return count
}

// we can use grid instead, get rid of map overhead
// Runtime: 5 ms
// Memory Usage: 3.9 MB
// T:O(m*n) T:O(1)
func numIslands20220924Optimized(grid [][]byte) int {
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(r, c int) bool
	dfs = func(r, c int) bool {
		rInBound := r >= 0 && r < len(grid)
		cInBound := c >= 0 && c < len(grid[0])
		if !(rInBound && cInBound) {
			return false
		}

		if grid[r][c] != '1' {
			return false
		}

		grid[r][c] = '2'

		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]
			row := r + dr
			col := c + dc
			dfs(row, col)
		}

		return true
	}

	count := 0
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			if grid[r][c] != '1' {
				continue
			}

			if dfs(r, c) {
				count += 1
			}
		}
	}

	return count
}

// Runtime: 44 ms
// Memory Usage: 7 MB
// T:O(m*n) T:O(m*n)
func numIslands20220924(grid [][]byte) int {
	visited := map[[2]int]bool{}
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(r, c int) bool
	dfs = func(r, c int) bool {
		rInBound := r >= 0 && r < len(grid)
		cInBound := c >= 0 && c < len(grid[0])
		if !(rInBound && cInBound) {
			return false
		}

		if grid[r][c] == '0' {
			return false
		}

		key := [2]int{r, c}
		if _, ok := visited[key]; ok {
			return false
		}

		visited[key] = true
		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]
			row := r + dr
			col := c + dc
			dfs(row, col)
		}

		return true
	}

	count := 0
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			if grid[r][c] == '0' {
				continue
			}

			if dfs(r, c) {
				count += 1
			}
		}
	}

	return count
}
