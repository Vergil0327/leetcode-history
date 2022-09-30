package main

func sequenceReconstruction(org []int, seqs [][]int) bool {
	nodes := map[int]bool{}
	for _, seq := range seqs {
		for _, node := range seq {
			nodes[node] = true
		}
	}
	inDegrees := map[int]int{}
	for node := range nodes {
		inDegrees[node] = 0
	}

	graph := map[int][]int{}
	for _, seq := range seqs {
		if len(seq) == 1 {
			graph[seq[0]] = make([]int, 0)
		}

		for i := 0; i < len(seq)-1; i++ {
			if graph[seq[i]] == nil {
				graph[seq[i]] = make([]int, 0)
			}
			if graph[seq[i+1]] == nil {
				graph[seq[i+1]] = make([]int, 0)
			}

			graph[seq[i]] = append(graph[seq[i]], seq[i+1])
			inDegrees[seq[i+1]] += 1
		}
	}

	queue := []int{}
	for node, deg := range inDegrees {
		if deg == 0 {
			queue = append(queue, node)
		}
	}

	order := make([]int, len(inDegrees))
	i := 0
	for len(queue) > 0 {
		// if true, we got more than 1 choice to generate topological order
		if len(queue) > 1 {
			return false
		}

		for _, node := range queue {
			queue = queue[1:]

			order[i] = node
			if order[i] != org[i] {
				return false
			}

			i += 1

			for _, nei := range graph[node] {
				inDegrees[nei] -= 1
				if inDegrees[nei] == 0 {
					queue = append(queue, nei)
				}
			}
		}
	}

	return len(order) == len(org)
}
