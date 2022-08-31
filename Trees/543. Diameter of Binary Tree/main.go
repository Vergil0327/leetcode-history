package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func dfs(root *TreeNode, diameter *int) int {
	if root == nil {
		return -1
	}

	heightL := dfs(root.Left, diameter)
	heightR := dfs(root.Right, diameter)
	*diameter = max(*diameter, heightL+heightR+2) // 2 -> every node has two edges between left & right node

	return 1 + max(heightL, heightR)
}

func diameterOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}

	diameter := 0
	dfs(root, &diameter)

	return diameter
}

// diameter = left node's level + right node's level
func diameterOfBinaryTreeCleaner(root *TreeNode) int {
	diameter := 0

	var depthFirstSearch func(node *TreeNode) int
	depthFirstSearch = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		left, right := depthFirstSearch(node.Left), depthFirstSearch(node.Right)
		diameter = max(diameter, left+right)

		return 1 + max(left, right)
	}

	depthFirstSearch(root)

	return diameter
}
