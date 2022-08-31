// https://leetcode.com/problems/redundant-connection/
package main

/*
https://leetcode.com/problems/redundant-connection/solution/

Approach #2: Union-Find [Accepted]
Intuition and Algorithm

If we are familiar with a Disjoint Set Union (DSU) data structure, we can use this in a straightforward manner to solve the problem: we simply find the first edge occurring in the graph that is already connected. The rest of this explanation will focus on the details of implementing DSU.

A DSU data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly. In particular, we would like to support two operations:

dsu.find(node x), which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component, and:

dsu.union(node x, node y), which draws an edge (x, y) in the graph, connecting the components with id find(x) and find(y) together.

To achieve this, we keep track of parent, which remembers the id of a smaller node in the same connected component. If the node is it's own parent, we call this the leader of that connected component.

A naive implementation of a DSU structure would look something like this:

Psuedocode in python

# parent initialized as (x -> x)
function find(x):
    while parent[x] != x: #While x isn't the leader
        x = parent[x]
    return x

function union(x, y):
    parent[find(x)] = find(y)

We use two techniques to improve the run-time complexity: path compression, and union-by-rank.

Path compression involves changing the x = parent[x] in the find function to parent[x] = find(parent[x]). Basically, as we compute the correct leader for x, we should remember our calculation.

Union-by-rank involves distributing the workload of find across leaders evenly. Whenever we dsu.union(x, y), we have two leaders xr, yr and we have to choose whether we want parent[x] = yr or parent[y] = xr. We choose the leader that has a higher following to pick up a new follower.
Specifically, the meaning of rank is that there are less than 2 ^ rank[x] followers of x. This strategy can be shown to give us better bounds for how long the recursive loop in dsu.find could run for.

class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge

Alternate Implementation of DSU without Union-By-Rank
class DSU:
    def __init__(self):
        self.par = range(1001)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

Complexity Analysis

Time Complexity: O(Nα(N))≈O(N), where N is the number of vertices (and also the number of edges) in the graph, and α is the Inverse-Ackermann function. We make up to N queries of dsu.union, which takes (amortized) O(α(N)) time. Outside the scope of this article, it can be shown why dsu.union has O(α(N)) complexity, what the Inverse-Ackermann function is, and why O(α(N)) is approximately O(1).

Space Complexity: O(N). The current construction of the graph (embedded in our dsu structure) has at most NN nodes.
*/

// Explanation: https://www.youtube.com/watch?v=FXWRE67PLL0
// UnionFind:如果 edges[i] = [u, v] 其中 u, v 的 root parent都是同一個，代表他們歸屬在同一類，已經是part of connected component
// 這時候在u跟v間再加上一個edge，就會形成cycle
func findRedundantConnection(edges [][]int) []int {
	parent := make([]int, len(edges)+1) // because n nodes start from 1
	for i := 0; i < len(parent); i++ {
		parent[i] = i // it means i node's parent is it self
	}

	rank := make([]int, len(edges)+1) // rank is upper bound of union-find size
	for i := 0; i < len(rank); i++ {
		rank[i] = 1
	}

	var find = func(n int) int {
		p := parent[n]

		// path compression
		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	// return false if we can't union n1 with n2
	var union = func(n1, n2 int) bool {
		p1, p2 := find(n1), find(n2)

		if p1 == p2 {
			return false
		}

		if rank[p1] > rank[p2] {
			parent[p2] = p1
			rank[p1] += rank[p2]
		} else {
			parent[p1] = p2
			rank[p2] += rank[p1]
		}

		return true
	}

	for _, edge := range edges {
		u, v := edge[0], edge[1]
		if !union(u, v) {
			return []int{u, v}
		}
	}

	return nil
}

/*
https://leetcode.com/problems/redundant-connection/solution/

Approach #1: DFS
Intuition and Algorithm

For each edge (u, v), traverse the graph with a depth-first search to see if we can connect u to v. If we can, then it must be the duplicate edge.

Complexity Analysis
Time Complexity: O(N^2) where N is the number of vertices (and also the number of edges) in the graph.
In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.

Space Complexity: O(N).
The current construction of the graph has at most N nodes.

python:
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
*/

func DFS(graph [][]int, start int, target int, visited map[int]bool) bool {
	if !visited[start] {
		visited[start] = true
		if start == target {
			return true
		}
		for _, nei := range graph[start] {
			if DFS(graph, nei, target, visited) == true {
				return true
			}
		}
	}
	return false
}

func findRedundantConnectionDFS(edges [][]int) []int {
	graph := make([][]int, 1001, 1001)
	ret := []int{}
	for _, edge := range edges {
		visited := make(map[int]bool)
		u, v := edge[0], edge[1]

		if len(graph[u]) != 0 && len(graph[v]) != 0 && DFS(graph, u, v, visited) {
			return edge
		}
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	return ret
}
