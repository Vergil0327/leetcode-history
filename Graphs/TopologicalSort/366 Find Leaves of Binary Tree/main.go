package main

type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}

// https://www.cnblogs.com/cnoodle/p/13557632.html
func findLeaves(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	res := [][]int{}

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return -1
		}

		depth := max(dfs(node.Left), dfs(node.Right)) + 1

		if depth+1 > len(res) {
			res = append(res, []int{})
		}

		res[depth] = append(res[depth], node.Val)

		return depth
	}

	dfs(root)
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
