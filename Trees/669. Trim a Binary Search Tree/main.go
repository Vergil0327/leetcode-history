package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// explanation: https://www.youtube.com/watch?v=jwt5mTjEXGc&ab_channel=NeetCode
func trimBST(root *TreeNode, low int, high int) *TreeNode {
	if root == nil {
		return nil
	}

	// handle edge case: root value might be out of bound
	if root.Val > high {
		return trimBST(root.Left, low, high)
	}

	if root.Val < low {
		return trimBST(root.Right, low, high)
	}

	// root is valid, but still need to update left & right subtree
	root.Left = trimBST(root.Left, low, high)
	root.Right = trimBST(root.Right, low, high)
	return root
}

func trimBST_FirstTry(root *TreeNode, low int, high int) *TreeNode {
	// find valid root first
	for root != nil {
		if root.Val < low {
			root = root.Right
		} else if root.Val > high {
			root = root.Left
		} else {
			break
		}
	}

	// trim leaf node by normal DFS
	var trim = func(root *TreeNode, low int, high int) *TreeNode {
		if root == nil {
			return nil
		}

		root.Left = trimBST(root.Left, low, high)
		root.Right = trimBST(root.Right, low, high)

		if root.Val < low {
			return nil
		}

		if root.Val > high {
			return nil
		}

		return root
	}

	return trim(root, low, high)
}
