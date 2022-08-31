package trees

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
	ret := make([]int, 0)
	st := make([](*TreeNode), 0)
	for len(st) > 0 || root != nil {
		if root != nil {
			st = append(st, root)
			root = root.Left
		} else {
			last := st[len(st)-1]
			st = st[:len(st)-1]
			ret = append(ret, last.Val)
			root = last.Right
		}
	}
	return ret
}
