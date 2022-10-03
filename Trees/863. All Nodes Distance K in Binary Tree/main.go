package main

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type KTreeNode struct {
	node *TreeNode
	k    int
}

// T:O(n) M:O(n)
func distanceK(root *TreeNode, target *TreeNode, k int) []int {
	parent := map[*TreeNode]*TreeNode{root: nil}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}

		if root.Left != nil {
			parent[root.Left] = root
			dfs(root.Left)
		}
		if root.Right != nil {
			parent[root.Right] = root
			dfs(root.Right)
		}
	}
	dfs(root)

	res := []int{}

	// graph BFS
	visited := map[*TreeNode]bool{} // avoid infinite parent.
	start := &KTreeNode{node: target, k: 0}
	queue := []*KTreeNode{start}
	for len(queue) > 0 {
		for _, knode := range queue {
			queue = queue[1:]

			if _, ok := visited[knode.node]; ok {
				continue
			}

			visited[knode.node] = true

			if knode.k == k {
				res = append(res, knode.node.Val)
			}

			if left := knode.node.Left; left != nil {
				queue = append(queue, &KTreeNode{node: left, k: knode.k + 1})
			}

			if right := knode.node.Right; right != nil {
				queue = append(queue, &KTreeNode{node: right, k: knode.k + 1})
			}

			if p := parent[knode.node]; p != nil {
				queue = append(queue, &KTreeNode{node: p, k: knode.k + 1})
			}
		}
	}

	return res
}
