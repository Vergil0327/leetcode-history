// https://leetcode.com/problems/build-a-matrix-with-conditions/

package main

/*
Example 1:
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.

Example 2:
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
*/

// explanation: https://leetcode.com/problems/build-a-matrix-with-conditions/discuss/2492822/Python3-topological-sort
func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
	// topological order of row
	graphR := map[int][]int{}
	indegreesR := make([]int, k)
	for _, rc := range rowConditions {
		u, v := rc[0], rc[1]
		if _, ok := graphR[u-1]; !ok {
			graphR[u-1] = make([]int, 0)
		}
		graphR[u-1] = append(graphR[u-1], v-1)
		indegreesR[v-1] += 1
	}

	queueRow := []int{}
	for u, deg := range indegreesR {
		if deg == 0 {
			queueRow = append(queueRow, u)
		}
	}

	orderRow := []int{}
	for len(queueRow) > 0 {
		for _, u := range queueRow {
			queueRow = queueRow[1:]
			orderRow = append(orderRow, u+1)

			for _, v := range graphR[u] {
				indegreesR[v] -= 1
				if indegreesR[v] == 0 {
					queueRow = append(queueRow, v)
				}
			}
		}
	}

	// topological order of col
	graphC := map[int][]int{}
	indegreesC := make([]int, k)
	for _, rc := range colConditions {
		u, v := rc[0], rc[1]
		if _, ok := graphC[u-1]; !ok {
			graphC[u-1] = make([]int, 0)
		}
		graphC[u-1] = append(graphC[u-1], v-1)
		indegreesC[v-1] += 1
	}

	queueCol := []int{}
	for u, deg := range indegreesC {
		if deg == 0 {
			queueCol = append(queueCol, u)
		}
	}

	orderCol := []int{}
	for len(queueCol) > 0 {
		for _, u := range queueCol {
			queueCol = queueCol[1:]
			orderCol = append(orderCol, u+1)

			for _, v := range graphC[u] {
				indegreesC[v] -= 1
				if indegreesC[v] == 0 {
					queueCol = append(queueCol, v)
				}
			}
		}
	}

	// check if there is any cycle in graph
	if len(orderRow) < k || len(orderCol) < k {
		return [][]int{}
	}

	matrix := make([][]int, k)
	for i := range matrix {
		matrix[i] = make([]int, k)
	}

	// orderRow: [1 3 2]
	// orderCol: [3 2 1]
	// add value according to order
	for r, vr := range orderRow {
		for c, vc := range orderCol {
			if vr == vc {
				matrix[r][c] = vr
				break
			}
		}
	}

	return matrix
}

// https://leetcode.com/problems/build-a-matrix-with-conditions/discuss/2492822/Python3-topological-sort
func buildMatrixBetter(k int, rowConditions [][]int, colConditions [][]int) [][]int {
	// topological order of row
	orderRow := topologicalSort(rowConditions, k)

	// topological order of col
	orderCol := topologicalSort(colConditions, k)

	// check if there is any cycle in graph
	if len(orderRow) < k || len(orderCol) < k {
		return [][]int{}
	}

	matrix := make([][]int, k)
	for i := range matrix {
		matrix[i] = make([]int, k)
	}

	// orderRow: [1 3 2]
	// orderCol: [3 2 1]
	// add value according to order
	rowMap := map[int]int{}
	for rol, v := range orderRow {
		rowMap[v] = rol
	}

	colMap := map[int]int{}
	for col, v := range orderCol {
		colMap[v] = col
	}

	// number range: 1-k
	for i := 1; i < k+1; i++ {
		matrix[rowMap[i]][colMap[i]] = i
	}

	return matrix
}

func topologicalSort(rules [][]int, k int) []int {
	graph := map[int][]int{}
	indegrees := make([]int, k)
	for _, r := range rules {
		u, v := r[0], r[1]
		if _, ok := graph[u-1]; !ok {
			graph[u-1] = make([]int, 0)
		}
		graph[u-1] = append(graph[u-1], v-1)
		indegrees[v-1] += 1
	}

	queue := []int{}
	for u, deg := range indegrees {
		if deg == 0 {
			queue = append(queue, u)
		}
	}

	order := []int{}
	for len(queue) > 0 {
		for _, u := range queue {
			queue = queue[1:]
			order = append(order, u+1)

			for _, v := range graph[u] {
				indegrees[v] -= 1
				if indegrees[v] == 0 {
					queue = append(queue, v)
				}
			}
		}
	}

	return order
}
