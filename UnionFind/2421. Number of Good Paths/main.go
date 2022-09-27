package main

import "sort"

// https://leetcode.com/discuss/interview-question/2260088/Special-Paths-or-Google-OA-or-July-2022-or-Graph
// https://leetcode.com/problems/number-of-good-paths/discuss/2620529/Python-Explanation-with-picture-DSU
// union-find
func numberOfGoodPaths(vals []int, edges [][]int) int {
	parent := make([]int, len(vals))
	rank := make([]int, len(vals))
	for i := range parent {
		parent[i] = i
		rank[i] = 1
	}

	var find func(node int) int = func(node int) int {
		p := parent[node]

		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	var union func(node1, node2 int) bool = func(node1, node2 int) bool {
		p1, p2 := find(node1), find(node2)
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

	// build adjacency list, T:O(n)
	graph := map[int][]int{}
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		if graph[u] == nil {
			graph[u] = make([]int, 0)
		}
		if graph[v] == nil {
			graph[v] = make([]int, 0)
		}
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	// T:O(nlogn)
	nodes := [][]int{} // [val, index]
	for i, v := range vals {
		nodes = append(nodes, []int{v, i})
	}
	sort.Slice(nodes, func(i, j int) bool { // sort by value in increasing order
		return nodes[i][0] < nodes[j][0]
	})

	// T:O(n) 
	count := map[int]map[int]int{} // index: [node_idx][node_value] = count, 在node_idx這個subtree底下, 有count個node_value node
	for node, v := range vals {
		if count[node] == nil {
			count[node] = make(map[int]int)
		}
		count[node][v] = 1
	}

	// T:O(E+V) = O(n), only 2 edges at most
	res := len(vals) // !!! each node itself is good_path
	for _, node := range nodes {
		val, curr := node[0], node[1]

		for _, nei := range graph[curr] {
			rootCurr, rootNei := find(curr), find(nei)
			if vals[nei] <= val && union(curr, nei) {
				root := find(curr)
				res += count[rootCurr][val] * count[rootNei][val] // if two subtree has same val of node, good_path += product of two count of subtree
				count[root][val] = count[rootCurr][val] + count[rootNei][val]
			}
		}
	}

	return res
}
