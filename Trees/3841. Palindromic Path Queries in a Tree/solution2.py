"""
In some competitive programming environments, HLD is preferred because it handles path-to-node updates and queries more directly than the "subtree range update" trick used in Euler Tours. If the problem were to change such that you update an entire path instead of just a single node, HLD would be the only way to go.

Why HLD might be "better"

1. Direct Path Logic: HLD decomposes any path into $O(\log N)$ contiguous segments. You don't have to worry about the "LCA bitmask correction" logic; you simply query the segments.
2. Versatility: It allows for more complex range updates on paths (like shifting characters) which a simple Fenwick Tree on an Euler Tour cannot do.

Optimized HLD Implementation
We will use a Fenwick Tree (or Segment Tree) to store the bitmasks of the nodes. Since we are only updating single nodes and querying paths, a Fenwick Tree is faster and more memory-efficient.

Feature    Heavy-Light Decomposition
Logic      Direct path segments ($O(\log N)$ segments)
Updates    $O(\log N)$
Queries    $O(\log^2 N)$ (with Fenwick)
Complexity More robust for path-based range updates

The "point" of Heavy-Light Decomposition (HLD) is to turn a complex, branching tree into a set of straight lines (paths).

Standard data structures like Fenwick Trees or Segment Trees are amazing at solving range queries on a flat array ($O(\log n)$). However, they don't work on trees because a path from node $A$ to node $B$ isn't a single contiguous range. HLD bridges this gap.

1. Why do we need it?

Imagine you are asked to:
1. Update the value of a node.
2. Find the sum (or XOR) of all nodes on the path between $u$ and $v$.

Without HLD, you might use a simple DFS/BFS for every query, which takes $O(n)$. If you have 50,000 queries, $50,000 \times 50,000$ is 2.5 billion operations—too slow. HLD allows you to do this in $O(\log^2 n)$, which is roughly 250 operations per query.

2. How it works: "The Heavy and the Light"

HLD splits the edges of the tree into two types:
- Heavy Edges: For each node, the edge leading to its child with the largest subtree is labeled "Heavy."
- Light Edges: All other edges are "Light."

By following only heavy edges, you form Heavy Chains.
Why this is clever:
1. Continuous Numbering: We relabel the nodes so that all nodes in a single Heavy Chain have consecutive indices (e.g., node 5, 6, 7, 8).
2. Few Jumps: A crucial mathematical property of HLD is that any path from the root to any node $v$ crosses at most $O(\log n)$ light edges. This means any path between any two nodes can be broken into at most $O(\log n)$ "straight" segments (heavy chains).

3. Why the Preprocessing?

We need the two-pass DFS preprocessing to "scout" the tree:
- First DFS: Calculates the size of each subtree and identifies which child is the heavy child.
- Second DFS: Actually builds the chains. It sets the head of each chain and assigns the position of each node in the flat array.

4. How the Query Works

When you want to query the path from $u$ to $v$:
1. Look at the head of the chains $u$ and $v$ belong to.
2. Pick the one whose head is deeper in the tree.
3. Query the range in your Fenwick/Segment tree from pos[head] to pos[u].
4. "Jump" $u$ up to the parent of its chain head.
5. Repeat until $u$ and $v$ are on the same chain.

Summary: The "Vibe"

Think of HLD as an express subway system.
- Heavy Chains are the fast subway lines. Once you're on one, you can fly through several stations (nodes) at once using a Segment Tree.
- Light Edges are the transfers. You can only have a logarithmic number of transfers before you reach your destination.
"""
class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # HLD Preprocessing
        parent = [-1] * n
        depth = [0] * n
        heavy = [-1] * n
        size = [1] * n

        def dfs_sz(u, p, d):
            parent[u] = p
            depth[u] = d
            max_subtree_sz = 0
            for v in adj[u]:
                if v != p:
                    sz = dfs_sz(v, u, d + 1)
                    size[u] += sz
                    if sz > max_subtree_sz:
                        max_subtree_sz = sz
                        heavy[u] = v
            return size[u]

        dfs_sz(0, -1, 0)

        head = [0] * n
        pos = [0] * n
        cur_pos = 0

        def dfs_hld(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs_hld(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs_hld(v, v)

        dfs_hld(0, 0)

        # Fenwick Tree on the HLD layout
        bit = [0] * (n + 1)
        def update(i, delta):
            i += 1
            while i <= n:
                bit[i] ^= delta
                i += i & (-i)

        def query(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & (-i)
            return res

        def query_range(l, r):
            if l > r: l, r = r, l
            return query(r) ^ query(l - 1)

        # Initial values
        current_chars = [1 << (ord(c) - ord('a')) for c in s]
        for i in range(n):
            update(pos[i], current_chars[i])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, char = int(parts[1]), parts[2]
                new_mask = 1 << (ord(char) - ord('a'))
                update(pos[u], current_chars[u] ^ new_mask)
                current_chars[u] = new_mask
            else:
                u, v = int(parts[1]), int(parts[2])
                res_mask = 0
                # Standard HLD path traversal
                while head[u] != head[v]:
                    if depth[head[u]] > depth[head[v]]:
                        res_mask ^= query_range(pos[head[u]], pos[u])
                        u = parent[head[u]]
                    else:
                        res_mask ^= query_range(pos[head[v]], pos[v])
                        v = parent[head[v]]
                
                res_mask ^= query_range(pos[u], pos[v])
                # Check palindrome parity
                ans.append((res_mask & (res_mask - 1)) == 0)

        return ans