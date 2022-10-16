package main

// https://leetcode.com/problems/create-components-with-same-value/discuss/2706736/Python-Explanation-with-pictures-BFS
func componentValue(nums []int, edges [][]int) int {
	if len(edges) == 0 {
		return 0
	}

	sum := 0
	for _, num := range nums {
		sum += num
	}

	inDegrees := make([]int, len(nums))
	graph := map[int][]int{}
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		if _, ok := graph[u]; !ok {
			graph[u] = make([]int, 0)
		}
		if _, ok := graph[v]; !ok {
			graph[v] = make([]int, 0)
		}
		graph[u] = append(graph[u], v)
		inDegrees[u] += 1
		graph[v] = append(graph[v], u)
		inDegrees[v] += 1
	}

	var topological = func(targetSum int) bool {
		queue := []int{}
		for node, deg := range inDegrees {
			// undirected graph, minimum deg is 1
			if deg == 1 {
				queue = append(queue, node)
			}
		}

		indeg := make([]int, len(inDegrees))
		copy(indeg, inDegrees)
		values := make([]int, len(nums))
		copy(values, nums)

		for len(queue) > 0 {
			for _, node := range queue {
				queue = queue[1:]

				if indeg[node] == 0 {
					continue
				}

				indeg[node] = 0

				// Edge case: if current value is target, don't push value to its parent.
				if values[node] == targetSum {
					for _, nei := range graph[node] {
						indeg[nei] -= 1
						if indeg[nei] == 1 {
							queue = append(queue, nei)
						} else if indeg[nei] == 0 { // Edge case: if its 'parent' is the last node, check if its value equals target.
							return values[nei] == targetSum
						}
					}
				} else { // Otherwise, we need to push its value to its parent.
					for _, nei := range graph[node] {
						indeg[nei] -= 1

						// merge value
						values[nei] += values[node]
						if indeg[nei] == 1 {
							queue = append(queue, nei)
						} else if indeg[nei] == 0 { // Edge case: if its the last node, check if its value equals target.
							return values[nei] == targetSum
						}
					}
				}
			}
		}

		return false
	}

	for targetSum := 1; targetSum <= sum; targetSum++ {
		if sum%targetSum == 0 && topological(targetSum) {
			groups := sum / targetSum
			return groups - 1
		}
	}

	return 0
}
