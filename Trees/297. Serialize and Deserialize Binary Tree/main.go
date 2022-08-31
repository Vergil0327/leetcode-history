// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
package main

import (
	"fmt"
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// testcases
// [1,2,3,null,null,4,5]
// []
// [1,2,3,null,null,4,5,6,7]

type Codec struct {
	tree *TreeNode
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 1
		}

		return 1 + dfs(root.Left) + dfs(root.Right)
	}
	length := dfs(root)

	list := []*TreeNode{}
	queue := []*TreeNode{root}
	for len(list) < length {
		for _, node := range queue {
			queue = queue[1:]
			if node != nil {
				if node.Left != nil {
					queue = append(queue, node.Left)
				} else {
					queue = append(queue, nil)
				}

				if node.Right != nil {
					queue = append(queue, node.Right)
				} else {
					queue = append(queue, nil)
				}
			}
			list = append(list, node)
		}
	}

	// trim right nil
	for i := len(list) - 1; i >= 0; i-- {
		if list[i] == nil {
			list = list[:len(list)-1]
		} else {
			break
		}
	}

	str := "["
	for i, node := range list {
		if i != 0 {
			str += ","
		}
		if node != nil {
			str += fmt.Sprintf("%d", node.Val)
		} else {
			str += "nil"
		}
	}
	str += "]"

	return str
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	data = data[1 : len(data)-1]
	if data == "" {
		return nil
	}

	serializedStrs := strings.Split(data, ",")

	val, _ := strconv.Atoi(serializedStrs[0])
	root := &TreeNode{Val: val}
	serializedStrs = serializedStrs[1:]

	curr := []*TreeNode{root}
	for len(serializedStrs) > 0 {
		for _, node := range curr {
			curr = curr[1:]
			if node == nil {
				continue
			}

			if len(serializedStrs) == 0 {
				break
			}

			node.Left = &TreeNode{}
			serializedStr := serializedStrs[0]
			serializedStrs = serializedStrs[1:]
			if serializedStr == "nil" {
				node.Left = nil
			} else {
				v, _ := strconv.Atoi(serializedStr)
				node.Left.Val = v
			}

			if len(serializedStrs) == 0 {
				break
			}

			node.Right = &TreeNode{}
			serializedStr = serializedStrs[0]
			serializedStrs = serializedStrs[1:]
			if serializedStr == "nil" {
				node.Right = nil
			} else {
				v, _ := strconv.Atoi(serializedStr)
				node.Right.Val = v
			}

			curr = append(curr, node.Left)
			curr = append(curr, node.Right)
		}
	}

	return root
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
