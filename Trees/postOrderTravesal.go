package trees

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postTraversal(root *TreeNode) []int {
	var out []int
	prev := root
	stack := []*TreeNode{root}

	for len(stack) > 0 {
		node := stack[len(stack)-1]
		if node.Left != nil && node.Left != prev && node.Right != prev {
			stack = append(stack, node.Left)
		} else if node.Right != nil && node.Right != prev {
			stack = append(stack, node.Right)
		} else {
			prev = node
			stack = stack[:len(stack)-1]
			out = append(out, node.Val)
		}
	}

	return out
}
