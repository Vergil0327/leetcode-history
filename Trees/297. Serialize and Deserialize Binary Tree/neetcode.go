// https://www.youtube.com/watch?v=u4JAi2JJhI8
package main

import (
	"strconv"
	"strings"
)

const NIL = "N"

// Serializes a tree to a single string.
func (this *Codec) serializeBetter(root *TreeNode) string {
	res := []string{}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			res = append(res, NIL)
			return
		}

		res = append(res, strconv.Itoa(root.Val))
		dfs(root.Left)
		dfs(root.Right)
	}

	dfs(root)

	return strings.Join(res, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserializeBetter(data string) *TreeNode {
	vals := strings.Split(data, ",")
	i := 0

	var dfs func() *TreeNode
	dfs = func() *TreeNode {
		if vals[i] == NIL {
			i += 1
			return nil
		}

		v, _ := strconv.Atoi(vals[i])
		node := &TreeNode{Val: v}
		i += 1

		node.Left = dfs()
		node.Right = dfs()

		return node
	}

	return dfs()
}

/*
func (this *Codec) deserialize(data string) *TreeNode {
	vals := strings.Split(data, ",")
	idx := 0

	var dfs func(i *int) *TreeNode
	dfs = func(i *int) *TreeNode {
		if vals[*i] == NIL {
			*i += 1
			return nil
		}

		v, _ := strconv.Atoi(vals[*i])
		node := &TreeNode{Val: v}
		*i += 1

		node.Left = dfs(i)
		node.Right = dfs(i)

		return node
	}

	return dfs(&idx)
}
*/
