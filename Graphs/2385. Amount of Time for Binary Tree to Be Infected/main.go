// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func amountOfTime(root *TreeNode, start int) int {
	adjList := map[int][]int{}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		if _, ok := adjList[root.Val]; !ok {
			adjList[root.Val] = make([]int, 0)
		}

		if root.Left != nil {
			if _, ok := adjList[root.Left.Val]; !ok {
				adjList[root.Left.Val] = make([]int, 0)
			}
			adjList[root.Val] = append(adjList[root.Val], root.Left.Val)
			adjList[root.Left.Val] = append(adjList[root.Left.Val], root.Val)

			dfs(root.Left)
		}
		if root.Right != nil {
			if _, ok := adjList[root.Right.Val]; !ok {
				adjList[root.Right.Val] = make([]int, 0)
			}
			adjList[root.Val] = append(adjList[root.Val], root.Right.Val)
			adjList[root.Right.Val] = append(adjList[root.Right.Val], root.Val)

			dfs(root.Right)
		}
	}
	dfs(root)

	minutes := 0
	visited := map[int]bool{}
	queue := []int{start}

	for len(queue) > 0 {
		for _, nodeVal := range queue {
			if _, ok := visited[nodeVal]; ok {
				continue
			}

			visited[nodeVal] = true

			for _, neighbor := range adjList[nodeVal] {
				if _, ok := visited[neighbor]; ok {
					continue
				}

				queue = append(queue, neighbor)
			}

			queue = queue[1:]
		}
		minutes += 1
	}

	return minutes - 1
}
