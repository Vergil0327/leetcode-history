package main

import (
	"strconv"
	"strings"
)

type Codec20220923 struct {
}

func Constructor20220923() Codec20220923 {
	return Codec20220923{}
}

// Serializes a tree to a single string.
func (this *Codec20220923) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}

	strs := []string{}

	queue := []*TreeNode{root}
	for len(queue) > 0 {
		for _, node := range queue {
			if node == nil {
				strs = append(strs, "N")
			} else {
				strs = append(strs, strconv.Itoa(node.Val))
			}

			if node != nil {
				queue = append(queue, node.Left)
				queue = append(queue, node.Right)
			}

			queue = queue[1:]
		}
	}

	return strings.Join(strs, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec20220923) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}

	nodes := []*TreeNode{}
	strs := strings.Split(data, ",")
	for _, s := range strs {
		var node *TreeNode = nil
		if s != "N" {
			val, _ := strconv.Atoi(s)
			node = &TreeNode{Val: val}
		}

		nodes = append(nodes, node)
	}

	root := nodes[0]
	nodes = nodes[1:]
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		for _, node := range queue {
			if node != nil && len(nodes) > 0 {
				left := nodes[0]
				nodes = nodes[1:]
				node.Left = left
				queue = append(queue, left)

				if len(nodes) > 0 {
					right := nodes[0]
					nodes = nodes[1:]
					node.Right = right
					queue = append(queue, right)
				}
			}
			queue = queue[1:]
		}
	}

	return root
}
