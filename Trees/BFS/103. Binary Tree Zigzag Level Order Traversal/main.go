// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/
package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// we can use only one for-loop
func zigzagLevelOrderOptimized(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	level := 0
	res := [][]int{}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		curr := make([]int, len(queue))
		size := len(queue)

		// BFS
		for idx, node := range queue {
			if level&1 == 0 {
				curr[idx] = node.Val
			} else {
				curr[size-1-idx] = node.Val
			}

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			queue = queue[1:]
		}

		level += 1
		res = append(res, curr)
	}

	return res
}

// check edge case in the beginning
// remove nested if clause
func zigzagLevelOrderConcise(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	level := 0
	res := [][]int{}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		curr := []int{}

		if level&1 == 0 {
			for i := 0; i < len(queue); i++ {
				curr = append(curr, queue[i].Val)
			}
		} else {
			for i := len(queue) - 1; i >= 0; i-- {
				curr = append(curr, queue[i].Val)
			}
		}

		// BFS
		for _, node := range queue {
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			queue = queue[1:]
		}

		level += 1
		res = append(res, curr)
	}

	return res

}

func zigzagLevelOrder(root *TreeNode) [][]int {
	level := 0
	res := [][]int{}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		curr := []int{}

		if level&1 == 0 {
			for i := 0; i < len(queue); i++ {
				if queue[i] != nil {
					curr = append(curr, queue[i].Val)
				}
			}
		} else {
			for i := len(queue) - 1; i >= 0; i-- {
				if queue[i] != nil {
					curr = append(curr, queue[i].Val)
				}
			}
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

		level += 1
		if len(curr) > 0 {
			res = append(res, curr)
		}
	}

	return res
}
