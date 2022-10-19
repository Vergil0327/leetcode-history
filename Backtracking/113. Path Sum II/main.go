package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	if root == nil {
		return nil
	}

	res := [][]int{}

	// state tracks current path
	var dfs func(state []int, target int, root *TreeNode)
	dfs = func(state []int, target int, root *TreeNode) {
		if root.Left == nil && root.Right == nil {
			if target == 0 {
				cpy := make([]int, len(state))
				copy(cpy, state)
				res = append(res, cpy)
			}
			return
		}

		if root.Left != nil {
			dfs(append(state, root.Left.Val), target-root.Left.Val, root.Left)
		}
		if root.Right != nil {
			dfs(append(state, root.Right.Val), target-root.Right.Val, root.Right)
		}
	}

	dfs([]int{root.Val}, targetSum-root.Val, root)

	return res
}
