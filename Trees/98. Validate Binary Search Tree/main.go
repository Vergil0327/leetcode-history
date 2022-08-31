// https://leetcode.com/problems/validate-binary-search-tree/
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

// Input: [2,1,3]
// Output: true
// Input: [5,1,4,null,null,3,6]
// Output: false
// Input: [2, 2, 2]
// Output: false
// Input: [5,4,6,null,null,3,7]
// Output: false

// Explanation: https://www.youtube.com/watch?v=s6ATEkipzow
// -Inf < root.Val < Inf
// left-side tree: -Inf < node.Val < root.Val, parentNode.Val, ...
// right-side tree: root.Val, parentNode.Val, ... < node.Val < Inf
// T:O(2n), 每個node會比較兩次 node.Val > left & node.Val < right
func isValidBST(root *TreeNode) bool {
	return check(root, math.MinInt, math.MaxInt)
}

// check if value is within left & right
func check(node *TreeNode, left, right int) bool {
	// base case: nil node is still valid
	if node == nil {
		return true
	}

	// parent-children comparison
	// this is the condition that breaks BST
	if !(node.Val > left && node.Val < right) {
		return false
	}

	isLeftSubTreeValid := check(node.Left, left, node.Val)
	isRightSubTreeValid := check(node.Right, node.Val, right)
	return isLeftSubTreeValid && isRightSubTreeValid
}
