package main

// 15
// 0
// [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
// [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
// expected: 3

// 1. construct our graph
// 2. we can see every headID as root node and use manager slice to find next headIDs
// 3. normal BFS traversal & accumulate every head's informTime
// 4. max(accumulate(informTime)) is what we want
// Time: O(n) since we traversal every employees
// Memory: O(n)
func numOfMinutesBFS(n int, headID int, manager []int, informTime []int) int {
	graph := map[int][]int{} // head: [id1, id2]
	for id, head := range manager {
		if head == -1 {
			continue
		}
		graph[head] = append(graph[head], id)
	}

	visited := map[int]bool{}
	visited[headID] = true
	time := 0
	queue := []int{headID}
	for len(queue) > 0 {
		for _, head := range queue {
			queue = queue[1:]

			time = max(time, informTime[head])

			for _, id := range graph[head] {
				if !visited[id] {
					visited[id] = true
					informTime[id] += informTime[head]
					queue = append(queue, id)
				}
			}
		}
	}

	return time
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

// just like top-down dfs traversal
// we accumulate max inform-time from leaf and recursively accumlate back to root
func numOfMinutesTopDown(n int, headID int, manager []int, informTime []int) int {
	graph := map[int][]int{} // head: [id1, id2]
	for id, head := range manager {
		if head == -1 {
			continue
		}
		graph[head] = append(graph[head], id)
	}

	var dfs func(headID int) int
	dfs = func(headID int) int {
		time := 0
		if _, ok := graph[headID]; !ok {
			return time
		}

		for _, managerID := range graph[headID] {
			time = max(time, dfs(managerID))
		}

		return time + informTime[headID]
	}
	return dfs(headID)
}

// bottom-up dfs, start from employees
// calculate every employee's inform time
// choose maximum
func numOfMinutesBottomUp(n int, headID int, manager []int, informTime []int) int {

	var dfs func(employeeID int) int // return inform time
	dfs = func(employeeID int) int {
		if managerID := manager[employeeID]; managerID != -1 {
			informTime[employeeID] += dfs(managerID)
			manager[employeeID] = -1 // mark: done the traversal and already accumulated inform time
		}

		return informTime[employeeID]
	}

	time := 0
	for id := range manager {
		time = max(time, dfs(id))
	}

	return time
}
