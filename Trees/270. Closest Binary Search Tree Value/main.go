package main

import "math"

type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}

func closestValue(root *TreeNode, target float64) int {
	res := float64(root.Val)

	curr := root
	for curr != nil {
		if math.Abs(float64(curr.Val)-target) < math.Abs(float64(res)-target) {
			res = float64(curr.Val)
		}

		if target > float64(curr.Val) {
			curr = curr.Right
		} else if target < float64(curr.Val) {
			curr = curr.Left
		} else {
			return curr.Val
		}
	}

	return int(res)
}
