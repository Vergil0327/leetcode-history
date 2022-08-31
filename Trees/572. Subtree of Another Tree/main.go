package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(root1, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}

	// if both are equal, check next node
	// else we know these two are not the same tree
	if root1 != nil && root2 != nil && root1.Val == root2.Val {
		return isSameTree(root1.Left, root2.Left) && isSameTree(root1.Right, root2.Right)
	}

	return false
}

// ? can ask if answer is true or false while subRoot is nil but root is not
// here we assume it's true while subRoot is nill
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	// the order matters, check subRoot first, then check if root is nil or not
	// if subRoot is nil, no matter what root is, all cases should be true
	if subRoot == nil {
		return true
	}

	// if root is nil after we've already check subRoot is not nil, it should return false
	// subTree can't be part of nil value
	if root == nil {
		return false
	}

	if isSameTree(root, subRoot) {
		return true
	}

	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}
