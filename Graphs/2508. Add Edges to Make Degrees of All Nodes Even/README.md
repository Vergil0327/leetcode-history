[2508. Add Edges to Make Degrees of All Nodes Even](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/description/)

`Hard`

There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.

You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return true if it is possible to make the degree of each node in the graph even, otherwise return false.

The degree of a node is the number of edges connected to it.

```
Example 1:
Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
Output: true
Explanation: The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.

Example 2:
Input: n = 4, edges = [[1,2],[3,4]]
Output: true
Explanation: The above diagram shows a valid way of adding two edges.

Example 3:
Input: n = 4, edges = [[1,2],[1,3],[1,4]]
Output: false
Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
```

Constraints:

- 3 <= n <= 10^5
- 2 <= edges.length <= 10^5
- edges[i].length == 2
- 1 <= ai, bi <= n
- ai != bi
- There are no repeated edges.

<details>
<summary>Hint 1</summary>

Notice that each edge that we add changes the degree of exactly 2 nodes.

</details>

<details>
<summary>Hint 2</summary>

The number of nodes with an odd degree in the original graph should be either 0, 2, or 4. Try to work on each of these cases.

</details>

<details>
<summary>Solution</summary>
[Lee215](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/solutions/2923720/python-stright-forward-with-explanation/?orderBy=most_votes)

```python
def isPossible(self, n, edges):
    G = [set() for i in range(n)]
    for i,j in edges:
        G[i-1].add(j-1)
        G[j-1].add(i-1)
    odd = [i for i in range(n) if len(G[i]) % 2]

    def f(a,b):
        return a not in G[b]

    if len(odd) == 2:
        a, b = odd
        return any(f(a,i) and f(b,i) for i in range(n))

    if len(odd) == 4:
        a,b,c,d = odd
        return  f(a,b) and f(c,d) or \
                f(a,c) and f(b,d) or \
                f(a,d) and f(c,b)
    return len(odd) == 0
```

</details>