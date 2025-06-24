# Intuition

how to find the k-th smallest distinct path XOR sum among all nodes in the subtree rooted at node-u?
post-order dfs?

hints:
1. For each node u, maintain the set of XOR values along the path from the root to u.
2. Use DSU on tree (small-to-large merging) during DFS to efficiently merge each child's set into its parent's set.
3. Store all XOR values in an ordered_set (in Python you can use the sortedcontainers module's SortedList) so you can quickly find the kth smallest XOR in any subtree.
4. At node u, process each query [u, k] by calling find_by_order(k − 1) (C++ PBDS) or indexing sorted_list[k-1] (Python SortedList).

backbone:

```py
class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(par)
        graph = [[] for _ in range(n)]
        root = None
        for node, p in enumerate(par):
            if p != -1:
                graph[p].append(node)
            else:
                root = node

        # Store the queries in a map for each node. then we can solve all the queries asscociated with a node in one go.
        queries_map = [[] for _ in range(n)]
        for i, (u, k) in enumerate(queries):
            queries_map[u].append((k, i))

        self.res = [-1] * len(queries)

        def dfs(node, path_xor):
            raise NotImplementedError("DFS logic needs to be implemented")

        dfs(root, 0)
        return self.res
```

再來依題意, 我們用SortedSet來排序, 並試著回答當前節點的k-th smallest:

```py
self.res = [-1] * len(queries)
def dfs(node, path_xor):
    cur = vals[node] ^ path_xor

    sl = SortedSet([cur])
    for child in graph[node]:
        sl_child = dfs(child, cur)
        sl |= sl_child  # Merge the sorted lists

    for k, idx in queries_map[node]:
        if k <= len(sl):
            self.res[idx] = sl[k - 1]
    return sl
```

但這樣會TLE

這邊有個可以優化的地方是, 我們**不要重新建立SortedSet**, 並且在merge的時候, 要讓**size較大的SortedSet去合併size較小的SortedSet**

這樣比起:

```py
sl |= sl_child
```

或是

```py
def merge(x1, x2):
    if len(x1) < len(x2):
        x2, x1 = x1, x2
    return x1 | x2
```

都會來的更有效率.

the idea of small to large merging: when you have to sets, simply merge the smaller one into the larger one.

Intuitively this will obviously be more efficient, you have to do less set add operations after all, but it isn't as intuitive why this allows for all of the sets to be merged in NLogN time total.

Here is why: consider two sets A and B and without loss of generality let set A be the smaller set with size X.
When we merge set A with set B, we will get a set that is at least size 2X. This means that everytime an element is merged from one set into another, the size of the set it belongs to will at least double. From this, we can observe that an element can only 'change' sets (i.e. be added into another set) at most Log(N) times.
Because for this problem, we are using sorted data structures, each set add operation takes Log(N) time. Thus, for each node the total sum of all set operations involving that node will take O(Log^2(N)) time.
There are N such nodes and thus our time complexity works out to be O(N * Log^2(N)).