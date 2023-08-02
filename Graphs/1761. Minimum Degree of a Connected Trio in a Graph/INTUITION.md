# Intuition

no idea initially, think brute force first

iterate node first -> if current node has 2 neighbors which are connected with each other, we found trio.
and we can just calculate their deg of connected trio by `sum(indegrees[trio_nodes[i]])-2*3`
and time will be $O(n^3)$ => it looks acceptable.

therefore,
1. iterate edges and iterate node from 1 to n
2. calculate their degree of connected trio

**Optimization**

we can sort node with its indegree. whenever we found a valid node, it must be smallest degree for current edge to construct a trio, we can break loop directly