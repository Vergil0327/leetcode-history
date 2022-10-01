package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// T:O(min(length(root1), length(root2)))
// M:O(min(length(root1), length(root2)))
func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
	// check nil first
	if root1 == nil || root2 == nil {
		return root1 == root2
	}

	// check value
	if root1.Val != root2.Val {
		return false
	}

	// check nil first
	if root1.Left == nil || root2.Left == nil {
		// if different, swap
		if root1.Left != root2.Left {
			root1.Left, root1.Right = root1.Right, root1.Left
		}
		return flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
	}

	// check nil first
	if root1.Right == nil || root2.Right == nil {
		// if different, swap
		if root1.Right != root2.Right {
			root1.Left, root1.Right = root1.Right, root1.Left
		}
		return flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
	}

	// check value
	if root1.Left.Val != root2.Left.Val || root1.Right.Val != root2.Right.Val {
		root1.Left, root1.Right = root1.Right, root1.Left
		return flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
	}

	return flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
}

func flipEquivConcise(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == root2 {
		return true
	}

	if root1 == nil || root2 == nil || root1.Val != root2.Val {
		return false
	}

	return (flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)) ||
		(flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left))
}
