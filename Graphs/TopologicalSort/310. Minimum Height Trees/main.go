package main

import "math"

// explanation: https://www.youtube.com/watch?v=2BaulnY_ssM&ab_channel=HuifengGuan
func findMinHeightTrees(n int, edges [][]int) []int {
	// edge case
	if n == 1 {
		return []int{0}
	}

	// edge case
	if n == 2 {
		return []int{0, 1}
	}

	graph := map[int][]int{}
	degrees := make([]int, n)

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
		degrees[u] += 1
		degrees[v] += 1
	}

	queue := []int{}
	for node, deg := range degrees {
		if deg == 1 /* outermost node */ {
			queue = append(queue, node)
		}
	}

	i := 0
	for len(queue) > 0 {
		for _, node := range queue {
			queue = queue[1:]

			i += 1

			for _, nei := range graph[node] {
				degrees[nei] -= 1
				if degrees[nei] == 1 {
					queue = append(queue, nei)
				}
			}
		}

		if i == n-1 || i == n-2 { // one or two more node left -> center node
			break
		}
	}

	return queue
}

// TLE
func findMinHeightTreesBruteForce(n int, edges [][]int) []int {
	if n == 1 {
		return []int{0}
	}

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

	var dfs func(root int, visited map[int]bool) int
	dfs = func(root int, visited map[int]bool) int {
		if _, ok := visited[root]; ok {
			return 0
		}

		visited[root] = true

		var h int
		for _, nei := range graph[root] {
			h = max(h, dfs(nei, visited))
		}

		return 1 + h
	}

	minH := math.MaxInt
	res := []int{}
	for node := range graph {
		val := dfs(node, map[int]bool{})

		if val < minH {
			minH = val
			res = []int{node}
		} else if val == minH {
			res = append(res, node)
		}
	}

	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
