// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
// Subscribe to UNLOCK
package main

// https://www.youtube.com/watch?v=8f1XPm4WOUc
func numberOfConnectedComponentUnionFind(edges [][]int, n int) int {
	parent := make([]int, n)
	for i := 0; i < len(parent); i++ {
		parent[i] = i
	}
	rank := make([]int, n)
	for i := 0; i < len(rank); i++ {
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

	// return false if we can't union n1, n2
	var union = func(n1, n2 int) bool {
		p1, p2 := find(n1), find(n2)
		if p1 == p2 /* already connected */ {
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

	for _, edge := range edges {
		e, v := edge[0], edge[1]
		if union(e, v) {
			n -= 1
		}
	}

	return n
}

func solution(edges [][]int, n int) int {
	graph := buildGraph(edges)
	count := 0
	visited := map[int]bool{}

	var dfs func(curr int) bool
	dfs = func(curr int) bool {
		if visited[curr] {
			return false
		}

		visited[curr] = true

		for _, neighbor := range graph[curr] {
			dfs(neighbor)
		}

		return true
	}

	for node := range graph {
		if dfs(node) {
			count += 1
		}
	}

	return count
}

func buildGraph(edges [][]int) map[int][]int {
	graph := map[int][]int{}
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		if _, ok := graph[u]; ok {
			graph[u] = make([]int, 0)
		}
		if _, ok := graph[v]; ok {
			graph[v] = make([]int, 0)
		}
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	return graph
}
