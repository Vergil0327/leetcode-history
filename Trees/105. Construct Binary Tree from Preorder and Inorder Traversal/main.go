// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
package main

/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

		 3
		9 20
nil nil 15 7


	 	       3
		 9          20
	1     2    15     7
21 22 23 24 25 26 27 28

[3, root], 9, 1, 21, 22, 2, 23, 4, 20, 15, 25, 26, 7, 27, 28
21, 1, 22, 9, 23, 2, 24, [3, root], 25, 15, 26, 20, 27, 7, 28
Output: 3, 9, 20, 1, 2, 15, 7, 21, 22, 23, 24, 25, 26, 27, 28

form inorder
left := 21, 1, 22, 9, 23, 2, 24
right := 25, 15, 26, 20, 27, 7, 28

Input: preorder = [-1], inorder = [-1]
Output: [-1]

*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func IndexOf[T comparable](collection []T, target T) int {
	for i, el := range collection {
		if el == target {
			return i
		}
	}
	return -1
}

// T: O(n^2) M:O(n^2)
// Explanation: https://www.youtube.com/watch?v=ihj4IQGZ2zc
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}

	root := &TreeNode{Val: preorder[0]}
	mid := IndexOf(inorder, root.Val)

	root.Left = buildTree(preorder[1:mid+1], inorder[:mid])
	root.Right = buildTree(preorder[mid+1:], inorder[mid+1:])
	return root
}

// T:O(n) M:O(N+logN) = O(n)
func buildTreeOptimize(preorder []int, inorder []int) *TreeNode {
	// T:O(n) M:O(n)
	inorderMap := map[int]int{}
	for i, v := range inorder {
		inorderMap[v] = i
	}

	rootIdx := 0

	// Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
	// Output: [3,9,20,null,null,15,7]
	// call stacks:
	// rootIdx, left, right
	// 0 0 4
	// 1 0 0
	// 2 2 4
	// 3 2 2
	// 4 4 4
	var array2tree func(left, right int) *TreeNode
	array2tree = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}

		root := &TreeNode{Val: preorder[rootIdx]}
		rootIdx += 1

		root.Left = array2tree(left, inorderMap[root.Val]-1)
		root.Right = array2tree(inorderMap[root.Val]+1, right)
		return root
	}

	return array2tree(0, len(preorder)-1)
}
