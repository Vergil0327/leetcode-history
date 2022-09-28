// https://leetcode.com/problems/course-schedule-ii/
package main

/*
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
*/

func findOrder(numCourses int, prerequisites [][]int) []int {
	// build graph (adjacency list) & inDegree list
	graph := make(map[int][]int)
	inDegrees := make([]int, numCourses)
	for _, coursePrerequisite := range prerequisites {
		pre, crs := coursePrerequisite[0], coursePrerequisite[1]
		graph[crs] = append(graph[crs], pre)

		inDegrees[pre] += 1
	}

	queue := []int{}
	for crs, inDegree := range inDegrees {
		if inDegree == 0 {
			queue = append(queue, crs)
		}
	}

	idx := 0
	order := []int{}
	for len(queue) > 0 {
		for _, crs := range queue {
			queue = queue[1:]
			order = append(order, crs)
			idx += 1

			for _, pre := range graph[crs] {
				inDegrees[pre] -= 1
				if inDegrees[pre] == 0 {
					queue = append(queue, pre)
				}
			}
		}
	}

	if idx == numCourses {
		return order
	} else {
		return []int{}
	}
}
