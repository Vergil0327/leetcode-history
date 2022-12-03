package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// T: O(logN), M: O(1)
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	lca := root

	for lca != nil {
		if p.Val > lca.Val && q.Val > lca.Val {
			lca = lca.Right
		} else if p.Val < lca.Val && q.Val < lca.Val {
			lca = lca.Left
		} else /* p, q on different side or one of p & q is root */ {
			return lca
		}
	}

	// must find lca somewhere, so it'll never run to this
	return nil
}

func lowestCommonAncestorRecursive(root, p, q *TreeNode) *TreeNode {
	if p.Val < root.Val && q.Val < root.Val {
		return lowestCommonAncestorRecursive(root.Left, p, q)
	}
	if p.Val > root.Val && q.Val > root.Val {
		return lowestCommonAncestorRecursive(root.Right, p, q)
	}

	// if p, q on different side or one of p & q is root
	return root
}
