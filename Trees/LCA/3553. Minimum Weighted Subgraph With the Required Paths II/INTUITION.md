# Intuition

[solution by @Alex Wice](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/solutions/6756302/python3-path-between-a-and-b-is-unique)

Important property: In a tree, a path between A and B is unique.

Consider CX, the shortest path from C to any node on the path AB. Using the important property, the shortest paths AB, AC, BC must be AXB AXC BXC. Therefore the required subgraph has weight AX + BX + CX, which is half of dist(A,B) + dist(A,C) + dist(B,C).

Let's calculate this using code. We use a BFS to populate up[k][u], depth[u], dist0[u]. This is the 2^k'th parent of u, the depth of u, and weighted distance from the root to u. We can find LCA and therefore dist(a, b) with standard techniques.