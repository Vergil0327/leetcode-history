package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode, isBalanced *bool) int {
	if root == nil {
		return 0
	}

	left := dfs(root.Left, isBalanced)
	right := dfs(root.Right, isBalanced)
	if math.Abs(float64(left)-float64(right)) > 1 {
		*isBalanced = false
	}

	return 1 + int(math.Max(float64(left), float64(right)))
}

// T:O(n)
func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}

	isBalanced := true
	dfs(root, &isBalanced)

	return isBalanced
}
