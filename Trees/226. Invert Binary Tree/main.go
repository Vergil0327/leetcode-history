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

func swap(node *TreeNode) *TreeNode {
	tmp := node.Left
	node.Left = node.Right
	node.Right = tmp
	return node
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	root = swap(root)
	root.Left = invertTree(root.Left)
	root.Right = invertTree(root.Right)
	return root
}
