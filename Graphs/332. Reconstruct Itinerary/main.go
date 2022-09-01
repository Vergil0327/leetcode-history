// https://leetcode.com/problems/reconstruct-itinerary/
package main

import "sort"

// https://www.youtube.com/watch?v=ZyB_gQ8vqGA
// backtracking
func findItinerary(tickets [][]string) []string {
	sort.Slice(tickets, func(i, j int) bool {
		if tickets[i][0] == tickets[j][0] {
			return tickets[i][1] < tickets[j][1]
		}

		return tickets[i][0] < tickets[j][0]
	})

	graph := make(map[string][]string)
	for _, ticket := range tickets {
		from, to := ticket[0], ticket[1]
		if _, ok := graph[from]; !ok {
			graph[from] = make([]string, 0)
		}
		graph[from] = append(graph[from], to)
	}

	itinerary := []string{"JFK"}

	var dfs func(from string) bool
	dfs = func(from string) bool {
		if len(itinerary) == len(tickets)+1 {
			return true
		}

		if _, ok := graph[from]; !ok {
			return false
		}

		cpy := make([]string, len(graph[from]))
		copy(cpy, graph[from])
		for i, v := range cpy {
			graph[from] = append(graph[from][:i], graph[from][i+1:]...)
			itinerary = append(itinerary, v)
			if dfs(v) {
				return true
			}

			// backtracking
			itinerary = itinerary[:len(itinerary)-1]
			graph[from] = append(append(graph[from][:i], v), graph[from][i:]...)
		}

		return false
	}
	dfs("JFK")

	return itinerary
}

// Euler Path Finding algorithm
// Hierholzer's algorithm
// https://leetcode.com/problems/reconstruct-itinerary/discuss/709590/Python-Short-Euler-Path-Finding-O(E-log-E)-explained.
// https://leetcode.com/problems/reconstruct-itinerary/discuss/359942/Awesome-question-or-new-algo-to-learn-or-Eulerian-Path-or-Full-explanation-or-Code
func findItineraryAlgorithm(tickets [][]string) []string {
	sort.Slice(tickets, func(i, j int) bool {
		if tickets[i][0] == tickets[j][0] {
			return tickets[i][1] < tickets[j][1]
		}

		return tickets[i][0] < tickets[j][0]
	})

	graph := make(map[string][]string)
	for _, ticket := range tickets {
		from, to := ticket[0], ticket[1]
		if _, ok := graph[from]; !ok {
			graph[from] = make([]string, 0)
		}
		graph[from] = append(graph[from], to)
	}

	itinerary := make([]string, len(tickets)+1)
	i := len(itinerary)

	var dfs func(from string)
	dfs = func(from string) {
		for len(graph[from]) > 0 {
			to := graph[from][0]
			graph[from] = graph[from][1:]
			dfs(to)
		}

		i -= 1
		itinerary[i] = from
	}
	dfs("JFK")

	return itinerary
}
