// https://leetcode.com/problems/binary-tree-level-order-traversal/
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
*/

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	queue := []*TreeNode{root}
	result := [][]int{}

	for len(queue) != 0 {
		list := []int{}
		for _, item := range queue {
			list = append(list, item.Val)
			queue = queue[1:]

			if item.Left != nil {
				queue = append(queue, item.Left)
			}
			if item.Right != nil {
				queue = append(queue, item.Right)
			}
		}

		result = append(result, list)
	}

	return result
}

func levelOrderBetter(root *TreeNode) [][]int {
	queue := []*TreeNode{root}
	result := [][]int{}

	for len(queue) != 0 {
		list := []int{}
		for _, node := range queue {
			if node != nil {
				list = append(list, node.Val)

				if node.Left != nil {
					queue = append(queue, node.Left)
				}
				if node.Right != nil {
					queue = append(queue, node.Right)
				}
			}
			queue = queue[1:]
		}

		if len(list) > 0 {
			result = append(result, list)
		}
	}

	return result
}
