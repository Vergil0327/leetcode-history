// https://leetcode.com/problems/course-schedule/
package main

// it's directed graph
// true if it's a directed acyclic graph
//
// adjacency list: { course: [prerequisite, ...]}
//
// Input: numCourses = 2, prerequisites = [[1,0]]
// adjacency list: {1: [0]}
// Output: true
//
// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// adjacency list: {1: [0], 0: [1]}
// Output: false because it got cycle

// T:O(n+p), n for every nodes we have & p for every prerequisites which mean all the edges
func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := buildGraph(prerequisites)
	visited := map[int]bool{}

	var dfs func(curr int) bool
	dfs = func(currCourse int) bool {
		// has cycle
		if visited[currCourse] {
			return false
		}

		// can finish course because it doesn't has prerequisties
		if len(graph[currCourse]) == 0 {
			return true
		}

		visited[currCourse] = true

		// DFS part
		for _, neighbor := range graph[currCourse] {
			if canFinish := dfs(neighbor); !canFinish {
				return false
			}
		}
		visited[currCourse] = false // ! just like backtracking. try another prerequisites and clean visited state after we checked the possibility

		// clean edges if course can be finished
		// become 2nd base case
		graph[currCourse] = []int{}

		return true
	}

	// loop through all the vertices and check if we can finish all the courses,
	// because it can be incomplete graph like this. not fully connected graph
	// ex. Input: numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
	for prerequisite := range graph {
		if !dfs(prerequisite) {
			return false
		}
	}

	return true
}

func buildGraph(prerequisites [][]int) map[int][]int {
	graph := make(map[int][]int)
	for _, prerequisite := range prerequisites {
		crs, pre := prerequisite[0], prerequisite[1]
		if _, ok := graph[crs]; !ok {
			graph[crs] = make([]int, 0)
		}
		graph[crs] = append(graph[crs], pre)
	}

	return graph
}

/* Another Solution: Topological sort */

/*
https://leetcode.com/problems/course-schedule/discuss/58516/Easy-BFS-Topological-sort-Java

According to the Wiki about what Topological sorting is (https://en.wikipedia.org/wiki/Topological_sorting)
and the Kahn's algorithm as shown below:
alt text
L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edges

while S is non-empty do
	remove a node n from S
	add n to tail of L

for each node m with an edge e from n to m do
	remove edge e from the graph
	if m has no other incoming edges then
		insert m into S

if graph has edges then
	return error (graph has at least one cycle)
else
	return L (a topologically sorted order)

Youtube Explanation: https://www.youtube.com/watch?v=cIBFEhD77b4
*/

func canFinishByTopologicalSort(numCourses int, prerequisites [][]int) bool {
	graph := buildGraph(prerequisites)

	inDegrees := make([]int, numCourses)
	for _, prerequisites := range graph {
		for _, prerequisite := range prerequisites {
			inDegrees[prerequisite] += 1
		}
	}

	// contains the set nodes with no incoming edges (0 in-degree)
	queue := []int{}
	for course, inDegree := range inDegrees {
		if inDegree == 0 {
			queue = append(queue, course)
		}
	}

	index := 0
	// order := make([]int, numCourses)
	for len(queue) > 0 {
		for _, crs := range queue {
			// order[index] = crs
			index += 1
			queue = queue[1:]

			for _, prerequisite := range graph[crs] {
				inDegrees[prerequisite] -= 1
				if inDegrees[prerequisite] == 0 {
					queue = append(queue, prerequisite)
				}
			}
		}
	}

	// if not equal, we has cycle in graph.
	// if equal, the order array is topological sorted array of graph
	return index == numCourses
}
