package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
// https://www.youtube.com/watch?v=aztbtN7JEg4&ab_channel=HuifengGuan
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	var LCA *TreeNode

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		count := 0
		if node == p || node == q {
			count += 1
		}

		left := dfs(node.Left)
		right := dfs(node.Right)

		// first LCA should be answer
		if isLCA := count+left+right == 2; isLCA && LCA == nil {
			LCA = node
			return count + left + right
		}

		return count + left + right
	}

	dfs(root)

	return LCA
}

// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65226/My-Java-Solution-which-is-easy-to-understand
func lowestCommonAncestorConcise(root, p, q *TreeNode) *TreeNode {
	if root == p || root == q || root == nil {
		return root
	}

	left := lowestCommonAncestor(root.Left, p, q)   // left subtree
	right := lowestCommonAncestor(root.Right, p, q) // right subtree

	if left == nil { // not in left subtree
		return right
	} else if right == nil { // not in right subtree
		return left
	} else {
		return root // either p or q. or ancestor when p, q exist in subtree
	}
}

// solution
func lowestCommonAncestor2(root, p, q *TreeNode) *TreeNode {
	// edge case
	// if we don't check this, stack would be empty and cause error
	// ex [1,2], p=1, q=2
	if p == root || q == root {
		return root
	}

	parent := map[*TreeNode]*TreeNode{root: nil}
	stack := []*TreeNode{root}

	for parent[p] == nil || parent[q] == nil {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if node.Left != nil {
			parent[node.Left] = node // While traversing the tree, keep saving the parent pointers.
			stack = append(stack, node.Left)
		}

		if node.Right != nil {
			parent[node.Right] = node // While traversing the tree, keep saving the parent pointers.
			stack = append(stack, node.Right)
		}
	}

	// Process all ancestors for node p using parent pointers.
	ancestor := map[*TreeNode]bool{}

	for p != nil {
		ancestor[p] = true
		p = parent[p]
	}

	// check if q is ancestor of p
	if _, ok := ancestor[q]; ok {
		return q
	}

	// find common ancestor of p and q
	for ancestor[q] == false {
		q = parent[q]
	}

	return q
}
