package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// explanation: https://www.youtube.com/watch?v=nHR8ytpzz7c&ab_channel=NeetCode
// O(n)
// 其實就是利用dynamic programming的概念持續透過DFS更新我們的返回值, dp = [rob root, NOT rob root]
func rob(root *TreeNode) int {
	// return (max value with Root, max value without Root)
	var dfs func(root *TreeNode) (withRoot, withoutRoot int)
	dfs = func(root *TreeNode) (withRoot int, withoutRoot int) {
		if root == nil {
			return 0, 0
		}

		withRootL, noRootL := dfs(root.Left)
		withRootR, noRootR := dfs(root.Right)

		return root.Val + noRootL + noRootR, max(withRootL, noRootL) + max(withRootR, noRootR)
	}

	return max(dfs(root))
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
