// https://leetcode.com/problems/count-good-nodes-in-binary-tree/
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

// Example 1:

// Input: root = [3,1,4,3,null,1,5]
// Output: 4
// Explanation: Nodes in blue are good.
// Root Node (3) is always a good node.
// Node 4 -> (3,4) is the maximum value in the path starting from the root.
// Node 5 -> (3,4,5) is the maximum value in the path
// Node 3 -> (3,1,3) is the maximum value in the path.
// Example 2:

// Input: root = [3,3,null,4,2]
// Output: 3
// Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
// Example 3:

// Input: root = [1]
// Output: 1
// Explanation: Root is considered as good.

// Input: [-1,5,-2,4,4,2,-2,null,null,-4,null,-2,3,null,-2,0,null,-1,null,-3,null,-4,-3,3,null,null,null,null,null,null,null,3,-3]
// Output: 5

// -1
// 5,-2
// 4,4,2,-2
// null,null,-4,null,-2,3,null,-2
// 0,null,-1,null,-3,null,-4,-3,3,null,null,null,null,null,null,null
// 3,-3

type Item struct {
	CurrentMax int
	Node       *TreeNode
}

func goodNodes(root *TreeNode) int {
	count := 0
	stack := []*Item{{Node: root, CurrentMax: math.MinInt}}

	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if pop.Node != nil {
			if pop.Node.Val >= pop.CurrentMax {
				count += 1
			}

			if pop.Node.Left != nil {
				item := &Item{Node: pop.Node.Left}
				item.CurrentMax = int(math.Max(float64(pop.CurrentMax), float64(pop.Node.Val)))
				stack = append(stack, item)
			}
			if pop.Node.Right != nil {
				item := &Item{Node: pop.Node.Right}
				item.CurrentMax = int(math.Max(float64(pop.CurrentMax), float64(pop.Node.Val)))
				stack = append(stack, item)
			}
		}
	}

	return count
}

func goodNodesRecursive(root *TreeNode) int {
	return dfs(root, root.Val)
}

func dfs(node *TreeNode, max int) int {
	if node == nil {
		return 0
	}

	result := 0
	if node.Val >= max {
		result += 1
	}
	max = int(math.Max(float64(max), float64(node.Val)))
	result += dfs(node.Left, max)
	result += dfs(node.Right, max)
	return result
}
