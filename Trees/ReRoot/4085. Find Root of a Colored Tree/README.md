[4085. Find Root of a Colored Tree](https://leetcode.com/problems/find-root-of-a-colored-tree/)

`Medium`

You are given an undirected tree of n nodes labeled from 0 to n - 1, represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an undirected edge between nodes ui and vi.

You are also given a string colors of length n, where colors[i] is one of 'R', 'B', or 'W', and denotes the color of node i.

A node chosen as root must satisfy both of the following conditions once the tree is oriented away from it:

1. Binary-tree property: Every node has at most two children.
2. Layered color pattern: All nodes at the same depth have the same color. Starting at depth 0, these colors follow one of the three repeating sequences:
    - R → B → W → R → B → W → ...
    - B → W → R → B → W → R → ...
    - W → R → B → W → R → B → ...
Return the index of any root that satisfies both conditions, or -1 if no such root exists.

A tree is a connected undirected graph with no cycles.

The depth of a node is the number of edges on the path from the root to that node. The root has depth 0. A child of a node is an adjacent node whose depth is one greater.

The degree of a node is the number of edges incident to it.

Example 1:
Input: edges = [[3,1],[3,2],[1,4],[2,0]], colors = "BRRWB"
Output: 3
Explanation:

![img](https://assets.leetcode.com/uploads/2025/06/15/treee.jpg)

Rooting at node 3 gives each node at most two children and every edge advances to the next color in the cycle (W → R → B), so return 3.

Example 2:
Input: edges = [[0,1],[1,2],[2,3]], colors = "RBRB"
Output: -1
Explanation:

![img](https://assets.leetcode.com/uploads/2025/06/15/treee2.jpg)

No root satisfies the required color step on every edge, so return -1.

Constraints:

- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i] = [ui, vi]
- 0 <= ui, vi < n
- colors.length == n
- colors[i] is one of 'R', 'B', 'W'.
- The input graph is a tree and every node has degree at most three.

Accepted
7,531/18K
Acceptance Rate
41.9%

<details>
<summary>Hint 1</summary>
1a (Forced Edge Orientations): Every parent-to-child edge must advance one step in the cycle R → B → W → R. Equal-colored endpoints make a solution impossible; otherwise, each edge has exactly one permitted direction.
</details>
<details>
<summary>Hint 2</summary>
1b (Forced Edge Orientations): A valid root must have indegree zero, and every other node must have indegree one. On a tree, these conditions ensure that all edges point away from the root.
</details>
<details>
<summary>Hint 3</summary>
1c (Forced Edge Orientations): The root must also have degree at most two. Every other node already has at most two children because its degree is at most three.
</details>
<details>
<summary>Hint 4</summary>
2a (Rerooting): Reject equal-colored edges. Root the tree arbitrarily and count edges whose child color is not the successor of the parent color.
</details>
<details>
<summary>Hint 5</summary>
2b (Rerooting): Moving the root across one edge reverses only that edge's parent-child direction. The number of incorrect edges increases by one if its old direction was correct, and decreases by one otherwise.
</details>
<details>
<summary>Hint 6</summary>
2c (Rerooting): Compute this count for every root in linear time. Return a node with no incorrect edges and degree at most two.
</details>