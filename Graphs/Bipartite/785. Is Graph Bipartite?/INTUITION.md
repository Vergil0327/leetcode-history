## DFS

first, let's define two groups `A` & `B` set
and we can use DFS to traverse every node to categorize nodes into 2 groups

case:
  1. if node is undefined, categorize to `A` and its neighbor to `B`
  2. if node belongs to `A`, then its neighbor must belong to  `B`, and vice versa

once we found invalid neighbor node, we just return `False` and don't need to traverse further

## Code

```py
def isBipartite(self, graph: List[List[int]]) -> bool:
    A, B = set(), set()
    visited = set()
    def dfs(node):
        if node in visited: return True
        visited.add(node)

        if node not in A and node not in B:
            A.add(node)

        for nei in graph[node]:
            if node in A:
                if nei in A: return False
                B.add(nei)
            else:
                if nei in B: return False
                A.add(nei)
            if not dfs(nei): return False
        return True

    for node, _ in enumerate(graph):
        if not dfs(node): return False
    return True
```

**Another way to solve**

we can use a `bool` array to categorize nodes. `True` or `False`

and we use `visited` to check if the neighbor has been categorized or not

- if we've visited neighbor once, check equality of current node and neighbor node
- if not, categorize neighbor to opposite group