// https://leetcode.com/problems/course-schedule/
package main

// ! can't check this
// Input: numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
// map[1:[13 15] 4:[17] 5:[5] 10:[0] 11:[6] 14:[11] 18:[3]]
// 1 -> 13
// 	 -> 15
// 4 -> 17
// 10 -> 0
// 14 -> 11 -> 6
// 18 -> 3
// 5 <-> 5 (self-loop)
func canFinishWRONG(numCourses int, prerequisites [][]int) bool {
	if len(prerequisites) < 1 {
		return true
	}

	graph := buildGraph(prerequisites)

	visited := map[int]bool{}

	// true means has cycle because traversal to visited vertice
	var dfs func(graph map[int][]int, curr int) bool
	dfs = func(graph map[int][]int, curr int) bool {
		if visited[curr] {
			return true
		}

		visited[curr] = true

		for _, neighbor := range graph[curr] {
			if dfs(graph, neighbor) {
				return true
			}
		}

		return false
	}

	return !dfs(graph, prerequisites[0][1])
}
