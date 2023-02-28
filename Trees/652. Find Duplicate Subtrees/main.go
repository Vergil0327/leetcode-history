package leetcode652

import "fmt"

/*
# Intuition

the target is to find duplicate subtree

in stead of using DFS to compare two subtree node by node, we can use post-order DFS and serialize each subtree's structure.

since we want to find duplicate subtree, we can use a hashmap to group subtree by its serialized structure.

once we found more than 1 subtree with same structure, we add it to our answer.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
*/

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	serials := map[string][]*TreeNode{}
	var dfs func(root *TreeNode) (*TreeNode, string)
	dfs = func(root *TreeNode) (*TreeNode, string) {
		if root == nil {
			return nil, "N"
		}

		left, serialL := dfs(root.Left)
		right, serialR := dfs(root.Right)

		serials[serialL] = append(serials[serialL], left)
		serials[serialR] = append(serials[serialR], right)

		return root, fmt.Sprintf("[%d-%s-%s]", root.Val, serialL, serialR)
	}
	dfs(root)

	res := []*TreeNode{}
	for serial, nodes := range serials {
		if len(nodes) > 1 && serial != "N" {
			res = append(res, nodes[0])
		}
	}
	return res
}
