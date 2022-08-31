// https://leetcode.com/problems/path-sum/
package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	var dfs func(root *TreeNode, sum int) bool
	dfs = func(root *TreeNode, sum int) bool {
		if root != nil && root.Left == nil && root.Right == nil && sum-root.Val == 0 {
			return true
		}

		if root == nil {
			return false
		}

		return dfs(root.Left, sum-root.Val) || dfs(root.Right, sum-root.Val)
	}

	return dfs(root, targetSum)
}
