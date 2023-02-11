# Intuition
since I want to find **shortest path**, come up with BFS quite naturally.
then, I start to consider the color constraint.

maybe I can use 2 BFS, 
1. start from red edge first, and keep going with alternating color
2. then start from blue edge first, and keep going  with alternating color

if I can reach `x`, current steps we used must be shortest path, and the `visited` hashset will prevent us from using same color edge twice to reach `x` node.

then I keep thinking, maybe I can combine these two BFS together by store extra information `color` in hashset

and I simulate the process:

if I can't reach it by red edge, I'll add `(x, RED)` to `visited`, and I'll never visited again by red edge.

if I can reach `x` by blue edge later, it still a valid shortest path.

now, the implementation should be easy. it's just normal BFS with `visited` hashset storing extra `color` information

# Complexity
- Time complexity:
$$O(N+E)$$

The complexity would be similar to the standard BFS algorithm since we’re iterating at most twice over each node.

Each queue operation in the BFS algorithm takes O(1) time, and a single node can only be pushed onto the queue twice, leading to O(n) operations for n nodes.

We iterate over all the neighbors of each node that is popped out of the queue, so for an undirected edge, a given edge could be iterated at most twice, resulting in O(e) operations total for all the nodes.

As a result, the total time required is O(n+e).

- Space complexity:
$$O(n+e)$$

- Building the adjacency list takes O(e) space.
- The BFS queue takes O(n) because each vertex is added at most twice in the form of triplet of integers.
- The other visit and answers arrays take O(n) space.
