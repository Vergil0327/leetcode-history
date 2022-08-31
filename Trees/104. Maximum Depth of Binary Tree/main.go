package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// recursive dfs solution: 1 + MAX(dfs(left), dfs(right))
// dfs: depth-first search
// T: O(n)
func maxDepthRecursion(root *TreeNode) int {
	if root == nil {
		return 0
	}

	if leftSubTree, rightSubTree := maxDepthRecursion(root.Left), maxDepthRecursion(root.Right); leftSubTree > rightSubTree {
		return 1 + leftSubTree
	} else {
		return 1 + rightSubTree
	}
	// return 1 + int(math.Max(float64(maxDepth(root.Left)), float64(maxDepth(root.Right))))
}

// iterative bfs solution
// bfs: breadth-first search
// T: O(n)
func maxDepthBFS(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lv := 0
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		for _, item := range queue {
			if item.Left != nil {
				queue = append(queue, item.Left)
			}
			if item.Right != nil {
				queue = append(queue, item.Right)
			}
			queue = queue[1:]
		}
		lv += 1
	}
	return lv
}

type Element struct {
	node  *TreeNode
	depth int
}

// iterative dfs solution
// bfs: depth-first search (pre-order)
// T: O(n)
func maxDepthDFS(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lv := 1
	stack := []*Element{{node: root, depth: 1}}
	for len(stack) > 0 {
		el := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if el.node != nil {
			lv = int(math.Max(float64(lv), float64(el.depth)))
			stack = append(stack, &Element{el.node.Left, el.depth + 1}, &Element{el.node.Right, el.depth + 1})
		}
	}

	return lv
}

func maxDepthDFSBetter(root *TreeNode) int {
	lv := 0
	stack := []*Element{{node: root, depth: 1}}
	for len(stack) > 0 {
		el := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if el.node != nil {
			lv = int(math.Max(float64(lv), float64(el.depth)))
			stack = append(stack, &Element{el.node.Left, el.depth + 1}, &Element{el.node.Right, el.depth + 1})
		}
	}

	return lv
}
