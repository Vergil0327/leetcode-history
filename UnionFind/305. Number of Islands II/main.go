package main

func numIslands(m, n int, positions [][]int) []int {
	res := []int{}
	if m == 0 || n == 0 || len(positions) == 0 {
		return res
	}

	parent := make([]int, m*n)
	rank := make([]int, m*n)
	for i := range parent {
		parent[i] = -1
	}
	unionSize := 0

	var find func(node int) int = func(node int) int {
		p := parent[node]
		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	var union func(node1, node2 int) int = func(node1 int, node2 int) int {
		p1, p2 := find(node1), find(node2)
		if p1 == p2 {
			return 0
		}

		if rank[p1] > rank[p2] {
			parent[p2] = p1
			rank[p1] += rank[p2]
		} else {
			parent[p1] = p2
			rank[p2] += rank[p1]
		}

		return -1
	}

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for _, pos := range positions {
		node := pos[0]*n + pos[1]
		r, c := pos[0], pos[1]
		parent[node] = node
		rank[node] = 1
		unionSize += 1

		for _, dir := range dirs {
			dr, dc := dir[0], dir[1]
			row, col := r+dr, c+dc

			rowInBounds := row >= 0 && row < m
			colInBounds := col >= 0 && col < n
			neighbor := row*n + col
			if rowInBounds && colInBounds && parent[neighbor] != -1 {
				unionSize += union(node, neighbor)
			}
		}

		res = append(res, unionSize)
	}

	return res
}
