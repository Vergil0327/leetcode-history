package main

// https://www.cnblogs.com/grandyang/p/5306162.html
type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}

// [2,1,3], p = 1
func inorderSuccessorIterative(root, p *TreeNode) *TreeNode {
	var res *TreeNode
	for root != nil {
		// 比p大的都有可能，持續逼近
		if root.Val > p.Val {
			res = root
			root = root.Left
		} else {
			root = root.Right
		}
	}

	return res
}
func inorderSuccessorRecursion(root, p *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val <= p.Val { // => successor must exist in right subtree
		return inorderSuccessorRecursion(root.Right, p)
	} else {
		// keep approaching, if left == nil, then last root should be successor
		left := inorderSuccessorRecursion(root.Left, p)
		if left == nil {
			return root
		} else {
			return left
		}
	}
}

func inorderSuccessor(root, p *TreeNode) *TreeNode {
	var parent, successor *TreeNode

	// inorder traversal
	var dfs func(root, p *TreeNode)
	dfs = func(root, p *TreeNode) {
		if root == nil {
			return
		}

		dfs(root.Left, p)
		if parent == p {
			successor = root
			return
		}
		parent = root
		dfs(root.Right, p)
	}
	dfs(root, p)

	return successor
}
