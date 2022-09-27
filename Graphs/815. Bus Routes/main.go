package main

// https://www.youtube.com/watch?v=gSr3ii4ipsk&ab_channel=HuifengGuan
func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}

	stop2Bus := map[int][]int{} // stop: [bus1, bus2, ...]
	for idx, route := range routes {
		for i := 0; i < len(route); i++ {
			if stop2Bus[route[i]] == nil {
				stop2Bus[route[i]] = make([]int, 0)
			}
			stop2Bus[route[i]] = append(stop2Bus[route[i]], idx)
		}
	}

	// O:(E+V) = O(n^2)
	numBuses := 0
	queue := []int{source}
	visitedStop := map[int]bool{}
	visitedBus := map[int]bool{} // we won't take same bus to target
	for len(queue) > 0 {
		for _, stop := range queue {
			queue = queue[1:]

			if stop == target {
				return numBuses
			}

			for _, bus := range stop2Bus[stop] {
				// we don't want to add old bus into the queue once again
				if visitedBus[bus] {
					continue
				}
				visitedBus[bus] = true

				for _, stp := range routes[bus] {
					if !visitedStop[stp] {
						visitedStop[stp] = true
						queue = append(queue, stp)
					}
				}
			}

		}
		numBuses += 1
	}

	return -1
}

// TLE
func numBusesToDestinationBruteForce(routes [][]int, source int, target int) int {
	// n*m
	busRoute := map[int][]int{} // bus: [route, ...]
	for idx, route := range routes {
		for i := 0; i < len(route); i++ {
			if busRoute[route[i]] == nil {
				busRoute[route[i]] = make([]int, 0)
			}
			busRoute[route[i]] = append(busRoute[route[i]], idx)
		}
	}

	// O:(E+V)
	numBuses := 0
	queue := []int{source}
	visited := map[int]bool{}
	for len(queue) > 0 {
		for _, node := range queue {
			queue = queue[1:]

			if node == target {
				return numBuses
			}

			for _, idx := range busRoute[node] {
				for _, nei := range routes[idx] {
					if !visited[nei] {
						visited[nei] = true
						queue = append(queue, nei)
					}
				}
			}
		}
		numBuses += 1
	}

	return -1
}
