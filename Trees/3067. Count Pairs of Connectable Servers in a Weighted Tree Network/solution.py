class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        def dfs(node, prev, total):
            cnt = total%signalSpeed == 0
            for wei, nxt in graph[node]:
                if nxt == prev: continue
                cnt += dfs(nxt, node, total+wei)
            return cnt

        res = [0] * n
        for root in range(n):
            presum_cnt = 0
            for wei, nxt in graph[root]:
                cnt = dfs(nxt, root, wei)
                res[root] += presum_cnt * cnt
                presum_cnt += cnt
        return res

