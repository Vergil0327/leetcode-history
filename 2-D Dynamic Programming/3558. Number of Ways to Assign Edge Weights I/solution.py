from collections import defaultdict, deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Build the adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dp = defaultdict(int)
        deepest = []
        visited = set()
        queue = deque([(1, 1, 0)]) # node, prev, parity
        while queue:
            deepest = list(map(lambda x: x[0], queue))
            next_dp = defaultdict(int)
            for _ in range(len(queue)):
                node, prev, parity = queue.popleft()
                if (node, prev, parity) in visited: continue
                visited.add((node, prev, parity))
                
                for neighbor in graph[node]:
                    if neighbor == prev: continue

                    if node == 1:
                        next_dp[neighbor, node, parity] = 1
                        next_dp[neighbor, node, parity^1] = 1
                    else:
                        next_dp[neighbor, node, parity] += dp[node, prev, parity]
                        next_dp[neighbor, node, parity] %= 1000000007

                        next_dp[neighbor, node, parity^1] += dp[node, prev, parity]
                        next_dp[neighbor, node, parity^1] %= 1000000007

                    queue.append((neighbor, node, parity))
                    queue.append((neighbor, node, parity ^ 1))
            if not queue: break
            dp = next_dp
        deepest = set(deepest)
        
        res = 0
        for node, prev, parity in dp:
            if node in deepest and parity==1:
                return dp[node, prev, parity]
        return res