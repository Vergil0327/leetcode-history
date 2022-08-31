// https://leetcode.com/problems/binary-tree-right-side-view/
package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	queue := []*TreeNode{root}
	result := []int{}
	for len(queue) > 0 {
		lastNode := queue[len(queue)-1]
		if lastNode != nil {
			result = append(result, lastNode.Val)
		}

		for _, node := range queue {
			if node != nil {
				if node.Left != nil {
					queue = append(queue, node.Left)
				}
				if node.Right != nil {
					queue = append(queue, node.Right)
				}
			}

			queue = queue[1:]
		}
	}

	return result
}
