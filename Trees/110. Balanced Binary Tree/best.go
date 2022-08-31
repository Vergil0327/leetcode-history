package main

func height(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lh := height(root.Left)
	if lh == -1 {
		return -1
	}
	rh := height(root.Right)
	if rh == -1 {
		return -1
	}

	switch lh - rh {
	case 1, 0:
		return lh + 1
	case -1:
		return rh + 1
	default:
		return -1
	}
}

/**
* Definition for a binary tree node.
* type TreeNode struct {
*     Val int
*     Left *TreeNode
*     Right *TreeNode
* }
 */
func isBalancedTree(root *TreeNode) bool {
	return -1 != height(root)
}
