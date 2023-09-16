# Intuition

we can construct weighted adjacency list

for u -> v, weight = 0.
for v -> u, weight = 1 because we need to reverse edge's direction.

then, we can use dfs on undirected graph by dfs(node, prev) and return the cost from node to all the other nodes.

Finally we return dfs(i, -1) for each node `i` as the root.

Time O(n), worst O(n^2)
Space O(n)

# Other Solution - Reroot

actually, we can see graph as a tree since each node only has 2 edges at most.

for current root node, we can use dfs to calculate its minimum reversal by giving edge weight:

from u -> v, weight = 0
from v -> u, weight = 1

and we can see if current root's reversal is `v`

its child's reversal should be `v - weight[node][child] + weight[child][node]`
```
     root
     /  \
child1  child2

if root -> child1, weight = 0 => it means the edge's direction is `root -> child1`
thus, when child1 is root node, we should reverse this edge

root-child2 edge is just the same idea as above disscusion

time: O(n)
space: O(n)
