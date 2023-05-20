package main

// T:O(len(equations) * len(queries))
func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	// construct graph
	weights := map[[2]string]float64{}
	graph := map[string][]string{}
	for i, eq := range equations {
		u, v := eq[0], eq[1]

		weights[[2]string{u, v}] = values[i]
		weights[[2]string{v, u}] = 1 / values[i]

		if graph[u] == nil {
			graph[u] = make([]string, 0)
		}
		if graph[v] == nil {
			graph[v] = make([]string, 0)
		}
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	res := []float64{}

	var dfs func(state float64, curr, end string, visited map[string]bool) bool
	dfs = func(state float64, curr, end string, visited map[string]bool) bool {
		if curr == end {
			res = append(res, state)
			return true
		}

		for _, nei := range graph[curr] {
			if !visited[nei] {
				visited[nei] = true

				state *= weights[[2]string{curr, nei}]
				if dfs(state, nei, end, visited) {
					return true
				}
				state /= weights[[2]string{curr, nei}] // backtracking
			}
		}
		return false
	}

	for _, q := range queries {
		u, v := q[0], q[1]

		if _, ok := graph[u]; !ok {
			res = append(res, -1)
			continue
		}
		if _, ok := graph[v]; !ok {
			res = append(res, -1)
			continue
		}
		if u == v {
			res = append(res, 1)
			continue
		}

		// traversal from u to v
		// edge case: if we can't reach, we must append -1
		// ex.
		// [["a","b"],["c","d"]]
		// [1.0,1.0]
		// [["a","c"],["b","d"],["b","a"],["d","c"]]
		if !dfs(1, u, v, map[string]bool{u: true}) {
			res = append(res, -1)
		}
	}

	return res
}
