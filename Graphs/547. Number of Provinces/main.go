// https://leetcode.com/problems/number-of-provinces/
package main

func findCircleNum(isConnected [][]int) int {
	total := len(isConnected)
	parent := make([]int, total)
	for i := 0; i < total; i++ {
		parent[i] = i
	}

	rank := make([]int, total)
	for i := 0; i < total; i++ {
		rank[i] = 1
	}

	var find = func(n int) int {
		p := parent[n]

		// path compression
		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	var union = func(n1, n2 int) bool {
		p1, p2 := find(n1), find(n2)

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

	provinces := 0
	for r := 0; r < len(isConnected); r++ {
		for c := 0; c < len(isConnected[0]); c++ {
			if isConnected[r][c] == 1 {
				if union(r, c) {
					provinces += 1
				}
			}
		}
	}

	// total city: len(isConnected[0])
	// group together after each union
	return len(isConnected) - provinces
}
