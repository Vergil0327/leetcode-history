package main

/*
572. Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubtree2(root *TreeNode, subRoot *TreeNode) bool {
	queue := []*TreeNode{root}

	for len(queue) != 0 {
		node := queue[0]
		queue = queue[1:]

		if node.Val == subRoot.Val {
			if isSameTree(node, subRoot) {
				return true
			}
		}

		if node.Left != nil {
			queue = append(queue, node.Left)
		}

		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}

	return false
}

func isSameTree2(first *TreeNode, second *TreeNode) bool {
	cur, cur2, stack, stack2 := first, second, []*TreeNode{}, []*TreeNode{}

	for cur != nil || len(stack) != 0 {
		for cur != nil {
			if cur2 == nil || cur.Val != cur2.Val {
				return false
			}
			stack, stack2 = append(stack, cur), append(stack2, cur2)
			cur, cur2 = cur.Left, cur2.Left
		}
		if cur2 != nil {
			return false
		}
		cur, cur2 = stack[len(stack)-1].Right, stack2[len(stack2)-1].Right
		stack, stack2 = stack[:len(stack)-1], stack2[:len(stack2)-1]
	}

	return true
}
