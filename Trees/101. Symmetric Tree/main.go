package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// https://www.youtube.com/watch?v=K7LyJTWr2yA
func isSymmetric(root *TreeNode) bool {
	var dfs func(left, right *TreeNode) bool
	dfs = func(left, right *TreeNode) bool {
		if left == nil || right == nil {
			return left == right // both must be nil
		}

		if left.Val != right.Val {
			return false
		}

		return dfs(left.Left, right.Right) && dfs(left.Right, right.Left)
	}

	return dfs(root.Left, root.Right)
}
