from sortedcontainers import SortedSet
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

        # Hint 2: small-to-large merge
        def merge(x1, x2):
            if len(x1) < len(x2):
                x2, x1 = x1, x2
            # Merge two sorted sets
            x1 |= x2
            return x1

        self.res = [-1] * len(queries)
        def dfs(node, path_xor):
            cur = vals[node] ^ path_xor

            sl = SortedSet([cur])
            for child in graph[node]:
                sl_child = dfs(child, cur)
                sl = merge(sl, sl_child)  # Merge the sorted lists

            for k, idx in queries_map[node]:
                if k <= len(sl):
                    self.res[idx] = sl[k - 1]
            return sl

        dfs(root, 0)
        return self.res