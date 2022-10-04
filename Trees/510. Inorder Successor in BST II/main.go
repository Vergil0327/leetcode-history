package main

type TreeNode struct {
	Val                 int
	Left, Right, Parent *TreeNode
}

func inorderSuccessor(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}

	var successor *TreeNode // can exist in right subtree or parent
	if node.Right != nil {
		successor = node.Right
		for successor != nil && successor.Left != nil {
			successor = successor.Left
		}
	} else {
		successor = node.Parent
		for successor != nil && successor.Val < node.Val {
			successor = successor.Parent
		}
	}

	return successor
}
