## DFS (visited + seen)

- use `visited` to make sure we don't DFS traversal backward. only visited each node once
- use `seen` to detect if we seen certain node twice during DFS traversal

the difference is:
- `visited` help us traversal whole graph only once
- `seen` help us to detect if we traversal in a cycle during each DFS traversal

if we can DFS traversal all the prerequisites without detecting a cycle, it means we can finish all the courses

ps. the post-order would be topological order in reverse order

## BFS (queue + indegrees)

store every node's indegree in `indegrees`, and we start traversal from outer-most node in graph, i.e. 0 indegree, one by one

at each iteration, we can reduce indegree of current node's neighbor and remove node with 0 indegree

if we can successfully traversal the whole graph, it means no cycle
if we left some node with indegrees in the end, it means the graph has cycle