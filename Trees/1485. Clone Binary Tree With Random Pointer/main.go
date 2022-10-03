package main

type TreeNode struct {
	Val                 int
	Left, Right, Random *TreeNode
}

func copyRandomBinaryTree(root *TreeNode) *TreeNode {
	clone := map[*TreeNode]*TreeNode{}
	random := map[*TreeNode]*TreeNode{}

	var dfs func(root *TreeNode) *TreeNode
	dfs = func(root *TreeNode) *TreeNode {
		if root == nil {
			return nil
		}

		if _, ok := clone[root]; ok {
			return clone[root]
		}

		random[root] = root.Random
		clone[root] = &TreeNode{Val: root.Val}

		clone[root].Left = dfs(root.Left)
		clone[root].Right = dfs(root.Right)

		return clone[root]
	}

	dfs(root)

	for node, randomNode := range random {
		clone[node].Random = clone[randomNode]
	}

	return clone[root]
}

// func array2tree(nums []int) *TreeNode {
// 	var helper func(i, n int) *TreeNode
// 	helper = func(i, n int) *TreeNode {
// 		var root *TreeNode
// 		if i < n {
// 			root = &TreeNode{Val: nums[i]}
// 			root.Left = helper(2*i+1, n)
// 			root.Right = helper(2*i+2, n)
// 		}

// 		return root
// 	}

// 	return helper(0, len(nums))
// }
