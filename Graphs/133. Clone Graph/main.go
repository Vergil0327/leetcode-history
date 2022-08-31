// https://leetcode.com/problems/clone-graph/
package main

/**
 * Definition for a Node.
 */
type Node struct {
	Val       int
	Neighbors []*Node
}

/*
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
*/

type srcNode = *Node
type dstNode = *Node

// explanation: https://www.youtube.com/watch?v=mQeF6bN8hMk
func cloneGraph(node *Node) *Node {
	clonedMap := map[srcNode]dstNode{}

	root := clone(node, clonedMap)

	return root
}

func clone(src *Node, clonedMap map[srcNode]dstNode) *Node {
	if src == nil {
		return nil
	}

	if node, ok := clonedMap[src]; ok {
		return node
	}

	dst := &Node{}
	clonedMap[src] = dst

	dst.Val = src.Val
	for _, neighbor := range src.Neighbors {
		dst.Neighbors = append(dst.Neighbors, clone(neighbor, clonedMap))
	}

	return dst
}

// iterative method
func cloneGraphQueue(node *Node) *Node {
	nodes := map[int]*Node{}
	visited := map[int]bool{}

	queue := []*Node{node}

	var res *Node = &Node{Val: node.Val, Neighbors: make([]*Node, 0)}
	nodes[node.Val] = res

	for len(queue) > 0 {
		next := queue[0]
		queue = queue[1:]

		if next == nil {
			continue
		}

		if visited[next.Val] {
			continue
		}

		newNode, ok := nodes[next.Val]
		if !ok {
			newNode = &Node{Val: next.Val, Neighbors: []*Node{}}
			nodes[next.Val] = newNode
		}

		for _, neighbor := range next.Neighbors {
			if _, ok := nodes[neighbor.Val]; !ok {
				newNeighbor := &Node{Val: neighbor.Val, Neighbors: []*Node{}}
				nodes[neighbor.Val] = newNeighbor
			}

			newNode.Neighbors = append(newNode.Neighbors, nodes[neighbor.Val])

			queue = append(queue, neighbor)
		}

		visited[next.Val] = true
	}
	return res
}
