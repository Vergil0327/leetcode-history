// subscribe to UNLOCK
// https://jettlee.gitbooks.io/leetcode/content/261-graph-valid-tree.html
package main

/* Question
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges. */

// solution: https://www.youtube.com/watch?v=bXsUuownnoQ

func graphValidTree(edges [][]int, n int) bool {
	parent := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = i
	}

	rank := make([]int, n)
	for i := 0; i < n; i++ {
		rank[i] = 1
	}

	var find = func(n int) int {
		p := parent[n]

		// path compressionif
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
			rank[p2] += p1
		}

		return true
	}

	unionComponents := 0
	for _, edge := range edges {
		n1, n2 := edge[0], edge[1]
		if !union(n1, n2) {
			return false
		} else {
			unionComponents += 1
		}
	}

	// !!! BE CAREFUL
	// UnionFind 只能找出有沒有cycle, 但無法確定是不是每個Node都連接
	// 如果有孤立的Node則會錯誤
	return len(edges) == n-1
	// or return n-unionComponents == 1 // valid if only one connected component
}
