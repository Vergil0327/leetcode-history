// https://leetcode.com/problems/kth-smallest-element-in-a-bst/
package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	postOrderList := []int{}
	dfs(root, &postOrderList)

	return postOrderList[k-1]
}

// result from in-order traversal of BST will be DESCENDING value array
func dfs(node *TreeNode, order *[]int) {
	if node == nil {
		return
	}

	dfs(node.Left, order)
	*order = append(*order, node.Val)
	dfs(node.Right, order)
}

func kthSmallestRecursive(root *TreeNode, k int) int {
	result := 0
	inorder(root, &k, &result)

	return result
}

// result from in-order traversal of BST will be DESCENDING value array
func inorder(node *TreeNode, k *int, result *int) {
	if node == nil {
		return
	}

	inorder(node.Left, k, result)
	*k -= 1
	if *k == 0 {
		*result = node.Val
	}
	inorder(node.Right, k, result)
}

// Explanation: https://www.youtube.com/watch?v=5LUXSvjmGCw
// in-order traversal iteratively
func kthSmallestOptimized(root *TreeNode, k int) int {
	n := 0

	curr := root
	stack := []*TreeNode{}
	for curr != nil || len(stack) > 0 {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}

		// curr reach nil, pop stack to get parent node
		p := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		n += 1
		if n == k {
			return p.Val
		}

		// curr go to parent node then go to right
		// next loop will go to left-most node
		// whole process will be in-order traversal
		curr = p
		curr = curr.Right
	}

	return -1
}
