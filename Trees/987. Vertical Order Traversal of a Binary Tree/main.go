package main

import "sort"

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func verticalTraversal(root *TreeNode) [][]int {
	pos := map[*TreeNode][2]int{root: {0, 0}}

	nodes := map[int][][]int{} // col : [val, row]
	nodes[0] = [][]int{{root.Val, 0}}

	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}

		if node.Left != nil {
			pos[node.Left] = [2]int{pos[node][0] + 1, pos[node][1] - 1}
			if nodes[pos[node.Left][1]] == nil {
				nodes[pos[node.Left][1]] = make([][]int, 0)
			}
			nodes[pos[node.Left][1]] = append(nodes[pos[node.Left][1]], []int{node.Left.Val, pos[node.Left][0]})
			dfs(node.Left)
		}

		if node.Right != nil {
			pos[node.Right] = [2]int{pos[node][0] + 1, pos[node][1] + 1}
			if nodes[pos[node.Right][1]] == nil {
				nodes[pos[node.Right][1]] = make([][]int, 0)
			}
			nodes[pos[node.Right][1]] = append(nodes[pos[node.Right][1]], []int{node.Right.Val, pos[node.Right][0]})
			dfs(node.Right)
		}
	}
	dfs(root)

	cols := []int{}
	for col := range nodes {
		cols = append(cols, col)
	}
	sort.Ints(cols)

	res := [][]int{}
	for _, col := range cols {
		sort.Slice(nodes[col], func(i, j int) bool {
			if nodes[col][i][1] == nodes[col][j][1] {
				return nodes[col][i][0] < nodes[col][j][0]
			}
			return nodes[col][i][1] < nodes[col][j][1]
		})

		vals := []int{}
		for _, node := range nodes[col] {
			vals = append(vals, node[0])
		}
		res = append(res, vals)
	}

	return res
}
