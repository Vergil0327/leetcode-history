// https://leetcode.com/problems/binary-tree-maximum-path-sum/
package main

import "math"

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// explanation: https://www.youtube.com/watch?v=Hr5cWUld4vU
func maxPathSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	max := root.Val

	// return max path sum without split
	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}

		leftMax := dfs(root.Left)
		rightMax := dfs(root.Right)

		// Compute path sum WITH split
		// ! [edge case] think this: [5,-3,-5]
		// ! max will be 5 rather than 5+(-3)+(-5)
		// ! we can't compare max with `float64(root.Val+leftMax+rightMax)` directly,
		// ! or `math.Max(float64(root.Val), float64(root.Val+leftMax+rightMax))`
		leftMax = int(math.Max(0, float64(leftMax)))
		rightMax = int(math.Max(0, float64(rightMax)))
		max = int(math.Max(float64(max), float64(root.Val+leftMax+rightMax)))

		// ! [edge case] think this: [5,-3,-5]
		// ! subMax will be 5 rather than 5+(-3)
		// ! we can't compare max with `currMaxSum := float64(root.Val+subMax)` directly
		// ! we should take subMax and only if subMax is greater than 0
		return root.Val + int(math.Max(float64(leftMax), float64(rightMax)))
	}

	dfs(root)
	return max
}
