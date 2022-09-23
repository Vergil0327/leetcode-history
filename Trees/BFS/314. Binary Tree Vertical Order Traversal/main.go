package main

import (
	"sort"
)

type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}

type NodeWithIndex struct {
	idx  int
	node *TreeNode
}

// nlogn, BFS
func verticalOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	// T:O(n)
	// [[3 0] [9 1] [20 2] [15 5] [7 6]]
	// [[9] [3 15] [20] [7]]
	//           0						            0
	//       -1			+1				==>   -1    0   1
	//  -1-1  -1+1,1-1  1+1		    -2  -1  0		1		2
	orderMap := map[int][]int{} // { idx: [idx, val1, val2, ...]}
	queue := []*NodeWithIndex{{node: root, idx: 0}}
	for len(queue) > 0 {
		for _, idxNode := range queue {

			// lazy init
			if orderMap[idxNode.idx] == nil {
				orderMap[idxNode.idx] = make([]int, 0)
				// append idx at first for sorting
				orderMap[idxNode.idx] = append(orderMap[idxNode.idx], idxNode.idx)
			}
			val := idxNode.node.Val
			orderMap[idxNode.idx] = append(orderMap[idxNode.idx], val)

			if idxNode.node.Left != nil {
				i := idxNode.idx - 1
				queue = append(queue, &NodeWithIndex{node: idxNode.node.Left, idx: i})
			}

			if idxNode.node.Right != nil {
				i := idxNode.idx + 1
				queue = append(queue, &NodeWithIndex{node: idxNode.node.Right, idx: i})
			}

			queue = queue[1:]
		}
	}

	// O(n)
	res := [][]int{}
	for _, v := range orderMap {
		res = append(res, v)
	}

	// O(nlogn)
	sort.Slice(res, func(i, j int) bool {
		return res[i][0] < res[j][0] // sort by index
	})

	// O(n), remove sorting index
	for i := range res {
		res[i] = res[i][1:]
	}

	return res
}

// https://www.youtube.com/watch?v=kqHNP6NTzME
// we want vertical oder
// use DFS to traversal each node and we'll get 2-dimension map
// if we see it in sorted by key in ascending order, it'll be just like
// col-0: row in ascending order
// col-1: row in ascending order
// col-2: row in ascending order
// col-3: row in ascending order
// and this is the answer we want
func verticalOrderDFS(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	map2Dim := map[int]map[int]int{} // { row(dfs height): { col: val } }, col-1 for left node and col+1 for right node
	var dfs func(node *TreeNode, row, col int)
	dfs = func(node *TreeNode, row, col int) {
		if node == nil {
			return
		}

		if map2Dim[col] == nil {
			map2Dim[col] = make(map[int]int)
		}
		map2Dim[col][row] = node.Val
		dfs(node.Left, row+1, col-1)
		dfs(node.Right, row+1, col+1)
	}
	dfs(root, 0, 0)

	// append in order by key
	sortedCol := []int{}
	for k := range map2Dim {
		sortedCol = append(sortedCol, k)
	}
	sort.Ints(sortedCol)

	ans := [][]int{}
	// nlogn + n
	for _, col := range sortedCol {
		m := map2Dim[col]
		sortedRow := []int{}
		for k := range m {
			sortedRow = append(sortedRow, k)
		}
		// sorting every nodes
		sort.Ints(sortedRow)

		cols := []int{}
		for _, row := range sortedRow {
			cols = append(cols, m[row])
		}
		ans = append(ans, cols)
	}

	return ans
}
