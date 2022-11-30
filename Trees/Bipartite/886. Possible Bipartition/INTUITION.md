### DFS

like leetcode 785. Is Graph Bipartite?

first, build our graph (adjacency list) from `dislikes = [[ai,bi], ...]`
*ps. this is a undirected graph, we must add edge to ai and bi simultaneously*

then we traverse each node to see if it's valid to group everyone correctly

once we found any one is invalid to group together, we return `False`

if we group everyone correctly, return `True`

**How to Group**

- if neighbor is visited, check!
- if not visited, group neighbors in different group compared to node

**How to Check**

- valid: node is in the group different with all the neighbors
- invalid: node and its neighbor are in the same group

### Union-Find

after we build the graph (the adjacency list)

we can iterate through whole graph and union each node's neighbors together

we choose first neighbor as root neighbor, union rest of neighbors

after each union step, we check if current node is in the same group with neighbor or not

if it is, it means we can't split to 2 groups
if it's not after we've process the whole graph, return True