package main

import "math"

type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}

type InfoNode struct {
	node     *TreeNode
	size     int
	min, max int
}

// https://www.youtube.com/watch?v=X0oXMdtUDwo&ab_channel=takeUforward
// Post-order Traversal
// if not BST
// - max(leftSize, rightSize)
// set leftBoundary: minimum value
// set rightBoundary: maximum value
func largestBSTSubtree(root *TreeNode) int {
	var largestBST func(root *TreeNode) *InfoNode
	largestBST = func(root *TreeNode) *InfoNode {
		// empty BST: size == 0
		if root == nil {
			return &InfoNode{node: root, size: 0, min: math.MaxInt, max: math.MinInt} // nil is valid BST, put absolutely valid value to min & max for any comparison
		}

		// get value from left & right subtree in post-order traversal
		left := largestBST(root.Left)
		right := largestBST(root.Right)

		// if current value is valid BST. which means left max value < current < right min value
		// update value space of BST
		if left.max < root.Val && root.Val < right.min {
			return &InfoNode{
				node: root,
				min:  max(root.Val, left.max),
				max:  min(root.Val, right.min),
				size: 1 + left.size + right.size,
			}
		}

		// can't be BST
		return &InfoNode{
			node: root,
			min:  math.MinInt,
			max:  math.MaxInt,
			size: max(left.size, right.size),
		}
	}

	return largestBST(root).size
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

// Brute Force, DFS + Validation
// T:O(n^2)
func largestBSTSubtreeBruteForce(root *TreeNode) int {
	var isValid func(root *TreeNode, left, right int) bool
	isValid = func(root *TreeNode, left, right int) bool {
		if root == nil {
			return true
		}

		if root.Val <= left || root.Val >= right {
			return false
		}

		return isValid(root.Left, left, root.Val) && isValid(root.Right, root.Val, right)
	}

	maxSize := -1

	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}

		size := 1 + dfs(root.Left) + dfs(root.Right)
		if isValid(root, math.MinInt, math.MaxInt) {
			if size > maxSize {
				maxSize = size
			}
		}

		return size
	}
	dfs(root)

	return maxSize
}
