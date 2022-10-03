package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func delNodesEasyUnderstand(root *TreeNode, to_delete []int) []*TreeNode {
	toDeleted := map[int]bool{}
	for _, v := range to_delete {
		toDeleted[v] = true
	}

	deleted := map[*TreeNode]bool{}
	parent := map[*TreeNode]*TreeNode{root: nil}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}

		if toDeleted[root.Val] {
			deleted[root] = true
		}

		if root.Left != nil {
			parent[root.Left] = root
			dfs(root.Left)
		}

		if root.Right != nil {
			parent[root.Right] = root
			dfs(root.Right)
		}
	}
	dfs(root)

	res := []*TreeNode{}

	// if root doesn't exist in deleted, append to res
	if _, ok := deleted[root]; !ok {
		res = append(res, root)
	}

	for node := range deleted {
		// disconnect
		if p := parent[node]; p != nil {
			if p.Left == node {
				p.Left = nil
			} else {
				p.Right = nil
			}
		}

		// edge case: check if any child node exists in deleted
		// ex. [1,2,null,4,3], [2,3]
		if node.Left != nil && !deleted[node.Left] {
			res = append(res, node.Left)
		}

		if node.Right != nil && !deleted[node.Right] {
			res = append(res, node.Right)
		}
	}

	return res
}

// Clever & Optimized
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	deleted := map[int]bool{}
	for _, v := range to_delete {
		deleted[v] = true
	}

	res := []*TreeNode{}

	var dfs func(root *TreeNode) *TreeNode
	dfs = func(root *TreeNode) *TreeNode {
		if root == nil {
			return nil
		}

		root.Left = dfs(root.Left)
		root.Right = dfs(root.Right)

		// NOT exist in to_deleted
		if _, ok := deleted[root.Val]; !ok {
			return root
		}

		// it is impossible for child node to exist in to_deleted
		// all the child nodes have been checked because we append in post-order
		if root.Left != nil {
			res = append(res, root.Left)
		}

		if root.Right != nil {
			res = append(res, root.Right)
		}

		return nil
	}

	root = dfs(root)
	if root != nil {
		res = append(res, root)
	}

	return res
}
