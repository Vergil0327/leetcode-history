"""
### Problem Analysis & Rerooting Strategy

1. Color Transition Rules:
   - The cyclic order of colors is R -> B -> W -> R.
   - For an edge (parent, child) to be valid, color(child) MUST be the immediate successor of color(parent).
   - Color mapping: R -> 0, B -> 1, W -> 2.
   - Child color is valid if `(color(child) - color(parent)) % 3 == 1`.
   - If `color(u) == color(v)`, it can NEVER form a valid parent-child relationship. We can immediately return -1.

2. Tree Orientation & Inverted Edges:
   - For any chosen root node `r`, every undirected edge in the tree gets a directed orientation away from `r`.
   - An edge (u, v) is "inverted" or "incorrect" if the directed edge from parent to child violates the successor rule `(color(child) - color(parent)) % 3 != 1`.
   - A root `r` satisfies the color pattern condition if and only if the number of inverted edges is 0.

3. Binary Tree Condition:
   - The degree of any node in the tree is at most 3 (given in constraints).
   - Every non-root node has 1 parent edge and at most 2 child edges, so it automatically has at most 2 children.
   - The root node `r` has 0 parent edges, so its number of children equals its total degree `degree(r)`.
   - Therefore, a root `r` is valid if and only if:
     1. Inverted edge count = 0
     2. `degree(r) <= 2`

4. Rerooting DP Algorithm:
   - Step 1: Check if any edge connects nodes with identical colors. If so, return -1.
   - Step 2: Choose an arbitrary root (e.g., node 0) and run a standard DFS to orient all edges away from node 0. Compute `bad_count`, the total number of inverted edges when rooted at 0.
   - Step 3: Run a second DFS (Rerooting DFS) to compute `bad_count` when the root moves from `u` to a neighbor `v`:
     - Moving the root from `u` to `v` ONLY flips the direction of the single edge `(u, v)`:
       - Old direction: `u -> v` (parent `u`, child `v`)
       - New direction: `v -> u` (parent `v`, child `u`)
     - Subtract old edge's invalidity status and add new edge's invalidity status to `bad_count`.
     - If `bad_count == 0` and `degree(v) <= 2`, return `v`.

=== COMPLEXITY ANALYSIS ===

1. Time Complexity:
   - Initial DFS (dfs_init): Visits every node and edge once -> O(N)
   - Rerooting DFS (dfs_reroot): Visits every node and edge once -> O(N)
   - Total Time Complexity: O(N), running in under 0.15s for N = 100,000.

2. Space Complexity:
   - Graph adjacency list: O(N)
   - Recursion stack: O(N)
   - Total Space Complexity: O(N) auxiliary space.
"""
from collections import defaultdict

class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        color_map = {'R': 0, 'B': 1, 'W': 2}
        col = [color_map[c] for c in colors]
        
        graph = defaultdict(list)
        degrees = [0] * n
        
        # Build adjacency list and check for identical-color endpoints
        for u, v in edges:
            if col[u] == col[v]:
                return -1
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
            
        def is_valid_edge(parent: int, child: int) -> bool:
            # Child color must be (parent_color + 1) % 3
            return (col[child] - col[parent]) % 3 == 1

        # Step 1: Compute initial invalid edge count when rooted at node 0
        bad_count = 0
        
        def dfs_init(u: int, p: int):
            nonlocal bad_count
            for v in graph[u]:
                if v != p:
                    if not is_valid_edge(u, v):
                        bad_count += 1
                    dfs_init(v, u)

        dfs_init(0, -1)

        # Check if root 0 is valid
        if bad_count == 0 and degrees[0] <= 2:
            return 0

        # Step 2: Rerooting DFS to test all possible roots in O(1) per transition
        ans = -1

        def dfs_reroot(u: int, p: int, current_bad: int):
            nonlocal ans
            if ans != -1:
                return
            
            for v in graph[u]:
                if v != p:
                    # Direction changes from (u -> v) to (v -> u)
                    old_valid = is_valid_edge(u, v)
                    new_valid = is_valid_edge(v, u)
                    
                    next_bad = current_bad
                    if not old_valid:
                        next_bad -= 1
                    if not new_valid:
                        next_bad += 1
                    
                    if next_bad == 0 and degrees[v] <= 2:
                        ans = v
                        return
                    
                    dfs_reroot(v, u, next_bad)

        dfs_reroot(0, -1, bad_count)
        return ans