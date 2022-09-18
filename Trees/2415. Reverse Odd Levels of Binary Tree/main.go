// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// The key to solving this problem recursively for each level independently, we have to pass in two nodes at the same level and these two nodes need to be the left most and right most nodes that have not been visited.
// Then keep tracking the level to sweep the node values at an odd level.
// it'll start swapping left-most & right-most node at same level
func reverseOddLevelsDFS(root *TreeNode) *TreeNode {
	var dfs func(left, right *TreeNode, level int)
	dfs = func(left, right *TreeNode, level int) {
		if left == nil || right == nil {
			return
		}

		if level%2 != 1 {
			left.Val, right.Val = right.Val, left.Val
		}

		dfs(left.Left, right.Right, level+1)
		dfs(left.Right, right.Left, level+1)
	}

	dfs(root.Left, root.Right, 0)
	return root
}

// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/discuss/2590130/Python3-BFS-and-DFS-with-line-by-line-comments.
func reverseOddLevelsOptimized(root *TreeNode) *TreeNode {
	queue := []*TreeNode{root}
	lv := 0
	for len(queue) > 0 {
		// swap value ad odd level
		if lv&1 == 1 {
			for i, j := 0, len(queue)-1; i < j; i, j = i+1, j-1 {
				queue[i].Val, queue[j].Val = queue[j].Val, queue[i].Val
			}
		}

		// regular BFS
		for _, node := range queue {
			queue = queue[1:]

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		// update level
		lv += 1
	}
	return root
}

func reverseOddLevels(root *TreeNode) *TreeNode {
	queue := []*TreeNode{root}
	lv := 1
	var prevQ []*TreeNode
	for len(queue) > 0 {
		prevQ = make([]*TreeNode, 0)

		oddLvQueue := []int{}
		for _, node := range queue {
			queue = queue[1:]

			prevQ = append(prevQ, node)
			if node.Left != nil {
				oddLvQueue = append(oddLvQueue, node.Left.Val)
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				oddLvQueue = append(oddLvQueue, node.Right.Val)
				queue = append(queue, node.Right)
			}
		}

		if lv&1 == 1 {
			for len(prevQ) > 0 {
				node := prevQ[0]
				prevQ = prevQ[1:]
				if node.Left != nil && len(oddLvQueue) > 0 {
					node.Left.Val = oddLvQueue[len(oddLvQueue)-1]
					oddLvQueue = oddLvQueue[:len(oddLvQueue)-1]
				}

				if node.Right != nil && len(oddLvQueue) > 0 {
					node.Right.Val = oddLvQueue[len(oddLvQueue)-1]
					oddLvQueue = oddLvQueue[:len(oddLvQueue)-1]
				}
			}
		}

		lv += 1
	}
	return root
}
