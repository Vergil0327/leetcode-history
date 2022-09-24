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
	clone := map[*Node]*Node{}

	root := cloneNode(node, clone)
	return root
}

func cloneNode(src *Node, clone map[*Node]*Node) *Node {
	if src == nil {
		return nil
	}

	// base case: we've already cloned
	if _, ok := clone[src]; ok {
		return clone[src]
	}

	clone[src] = &Node{Val: src.Val, Neighbors: make([]*Node, 0)}
	for _, nei := range src.Neighbors {
		clone[src].Neighbors = append(clone[src].Neighbors, cloneNode(nei, clone))
	}

	return clone[src]
}

// iterative method
func cloneGraphQueue(node *Node) *Node {
	if node == nil {
		return nil
	}

	clone := map[*Node]*Node{}
	visited := map[*Node]bool{}

	queue := []*Node{node}
	for len(queue) > 0 {
		for _, n := range queue {
			queue = queue[1:]

			if visited[n] {
				continue
			}

			visited[n] = true

			if _, ok := clone[n]; !ok {
				clone[n] = &Node{Val: n.Val, Neighbors: make([]*Node, 0)}
			}

			for _, nei := range n.Neighbors {
				if _, ok := clone[nei]; !ok {
					clone[nei] = &Node{Val: nei.Val, Neighbors: make([]*Node, 0)}
				}
				clone[n].Neighbors = append(clone[n].Neighbors, clone[nei])

				queue = append(queue, nei)
			}
		}
	}

	return clone[node]
}
