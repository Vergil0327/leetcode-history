"""
### Mathematical Groundwork

For any two integers $A$ and $B$, the parity of set bits satisfies:
$$\text{popcount}(A \oplus B) \equiv \text{popcount}(A) + \text{popcount}(B) \pmod 2$$

Extending this to any path $u_1 - u_2 - \dots - u_k$:
$$\text{popcount}\left(\bigoplus_{i=1}^k \text{values}[u_i]\right) \equiv \bigoplus_{i=1}^k \Big(\text{popcount}(\text{values}[u_i]) \pmod 2\Big) \pmod 2$$

Let $p(u) = \text{popcount}(\text{values}[u]) \pmod 2 \in \{0, 1\}$.
A path is **Balanced-XOR** if and only if the XOR sum of the node parities along the path is **0**:
$$\bigoplus_{i=1}^k p(u_i) = 0$$

Since distinct endpoints are required, every valid path must contain at least 1 edge ($k \ge 2$).

### Solution 1: Local Paths (Explanation)

1. Parity Reduction:
   For any path u_1 - u_2 - ... - u_k, the XOR sum of node values has an even 
   popcount if and only if:
       p(u_1) ^ p(u_2) ^ ... ^ p(u_k) == 0
   where p(x) = popcount(values[x]) % 2.

2. At Most 2 Edges Needed:
   Because edge costs are strictly positive (c_i >= 1):
   - A 1-edge path (u, v) is balanced if and only if p[u] == p[v] (cost = c).
   - If any longer balanced path contains an edge with p[u] == p[v], using 
     just that single edge yields a balanced path with strictly smaller cost.
   - Therefore, any candidate path with >= 2 edges must alternate in parities 
     (0 - 1 - 0 - 1 ...).
   - An alternating path has an XOR sum of 0 if and only if it contains an 
     even number of 1s (at least two 1s).
   - The shortest such path is strictly 1 - 0 - 1 (a center node w with 
     p[w] == 0 connected to two distinct neighbors with p == 1).
   - Any longer alternating balanced path contains a 1 - 0 - 1 subpath, which 
     is already balanced and has strictly smaller cost.

3. Algorithm:
   - Check all edges (u, v) with p[u] == p[v].
   - For every node w with p[w] == 0, find the two cheapest incident edges 
     leading to distinct neighbors with p == 1, and take their sum.
   - Return the minimum cost found, or -1 if no such path exists.

=== Complexity Analysis ===

1. Time Complexity: O(n)
   - bit_count() runs in O(1) per value.
   - Inspecting edges takes O(n) time.
   - Scanning incident edges per node visits each directed edge once: O(n) time.
   - Overall Time Complexity: O(n), running in ~0.15s for n = 100,000.

2. Space Complexity: O(n)
   - Adjacency list storing n - 1 edges: O(n) auxiliary space.
   - Parity array p of size n: O(n) auxiliary space.
"""
class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        n = len(values)
        # Precompute parity of set bits for each node (0 or 1)
        p = [val.bit_count() % 2 for val in values]
        
        ans = float('inf')
        adj = [[] for _ in range(n)]
        
        # 1. Check all balanced 1-edge paths (p[u] == p[v])
        for u, v, c in edges:
            if p[u] == p[v]:
                ans = min(ans, c)
            adj[u].append((v, c))
            adj[v].append((u, c))
            
        # 2. Check 2-edge paths: 1 - 0 - 1
        for w in range(n):
            if p[w] == 0:
                # Find the two cheapest edges leading to neighbors with parity 1
                min1 = float('inf')
                min2 = float('inf')
                for nxt, cost in adj[w]:
                    if p[nxt] == 1:
                        if cost < min1:
                            min2 = min1
                            min1 = cost
                        elif cost < min2:
                            min2 = cost
                if min2 != float('inf'):
                    ans = min(ans, min1 + min2)
                    
        return ans if ans != float('inf') else -1


"""
### Solution 2: Tree DP (Explanation)

1. Parity Reduction:
   A path is Balanced-XOR if and only if the cumulative XOR sum of the node 
   parities along the path is 0:
       p(u_1) ^ p(u_2) ^ ... ^ p(u_k) == 0
   where p(x) = popcount(values[x]) % 2.

2. DP State Definition:
   Root the tree arbitrarily at node 0.
   For each node u, we define:
       dp[u][parity] = minimum cost of a downward path starting at node u 
                       whose XOR parity of node values is `parity` (0 or 1).

   Base Case at node u:
   A single-node path containing only u has cost 0 and parity p[u]:
       dp[u][p[u]] = 0
       dp[u][1 - p[u]] = inf

3. State Transitions (Child-by-Child Processing):
   When processing a child v connected to u via an edge of cost c:

   a. Combine Paths through u:
      An existing path starting at u with parity P1 and a downward path from 
      child v with parity P2 form a complete path between two distinct nodes 
      across edge (u, v):
          Total Parity = P1 ^ P2
          Total Cost   = dp[u][P1] + dp[v][P2] + c
      To satisfy the Balanced-XOR condition, we need P1 ^ P2 == 0 (i.e., P1 == P2).
      Therefore, for parity in {0, 1}:
          ans = min(ans, dp[u][parity] + dp[v][parity] + c)

   b. Extend Downward Paths from v to u:
      A downward path starting at v with parity P2 and cost dp[v][P2] can be 
      extended to start at u via edge (u, v):
          New Parity = p[u] ^ P2
          New Cost   = dp[v][P2] + c
      Update dp[u]:
          dp[u][p[u] ^ P2] = min(dp[u][p[u] ^ P2], dp[v][P2] + c)

=== Complexity Analysis ===

1. Time Complexity: O(n)
   - Precomputing bit_count takes O(1) per node -> O(n).
   - DFS visits each node and traverses each edge exactly once.
   - For each child, combining paths and updating states takes O(1) operations.
   - Total Time Complexity: O(n), running in ~0.20s for n = 100,000.

2. Space Complexity: O(n)
   - Adjacency list storage: O(n).
   - Recursion stack depth in the worst case (line tree): O(n).
   - Total Space Complexity: O(n) auxiliary space.
"""
import sys

# Increase recursion limit for deep tree test cases
sys.setrecursionlimit(200000)

class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        n = len(values)
        p = [val.bit_count() % 2 for val in values]
        
        adj = [[] for _ in range(n)]
        for u, v, c in edges:
            adj[u].append((v, c))
            adj[v].append((u, c))
            
        ans = float('inf')
        
        def dfs(u: int, parent: int) -> list[int]:
            nonlocal ans
            
            # dp_u[parity]: min cost of a downward path starting at u
            dp_u = [float('inf'), float('inf')]
            dp_u[p[u]] = 0
            
            for v, c in adj[u]:
                if v == parent:
                    continue
                
                dp_v = dfs(v, u)
                
                # 1. Combine paths: P1 ^ P2 == 0 requires P1 == P2
                for parity in (0, 1):
                    if dp_u[parity] != float('inf') and dp_v[parity] != float('inf'):
                        ans = min(ans, dp_u[parity] + dp_v[parity] + c)
                        
                # 2. Extend downward path from child v to node u
                for parity in (0, 1):
                    if dp_v[parity] != float('inf'):
                        new_parity = p[u] ^ parity
                        dp_u[new_parity] = min(dp_u[new_parity], dp_v[parity] + c)
                        
            return dp_u
        
        dfs(0, -1)
        return ans if ans != float('inf') else -1