class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [0] * n
        def dfs(node, prev, target):
            if node == target:
                return True

            for nei in graph[node]:
                if nei == prev: continue
                if dfs(nei, node, target):
                    count[nei] += 1
                    return True
            return False

        for trip in trips:
            u, v = trip
            count[u] += 1
            dfs(u, u, v)

        # house-robber
        @lru_cache(None)
        def dp(node, prev, isHalf):
            currentPrice = count[node]*price[node]
            if isHalf:
                currentPrice //= 2


            res = 0
            for nei in graph[node]:
                if nei == prev: continue
                if isHalf:
                    res += dp(nei, node, False)
                else:
                    res += min(dp(nei, node, True), dp(nei, node, False))
            
            return res + currentPrice

        res = inf
        for node in range(n):
            res = min(res, min(dp(node, node, True), dp(node, node, False)))
        return res